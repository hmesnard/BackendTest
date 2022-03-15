import os
import importlib.machinery
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PackageSerializer, UploadSerializer
from .models import Package

aapt = importlib.machinery.SourceFileLoader('aapt', str(os.getenv('AAPT_DIR')) + 'aapt/aapt.py').load_module()

class PackageView(APIView):

    serializer_class = UploadSerializer

    def get(self, request):
        packages = Package.objects.all()
        packageSerializer = PackageSerializer(packages, many=True)
        return Response(packageSerializer.data)

    def post(self, request, format=None):
        uploadSerializer = UploadSerializer(data = request.data)
        if (not uploadSerializer.is_valid()):
            return Response(uploadSerializer.errors, status = status.HTTP_400_BAD_REQUEST)

        uploadFile = request.FILES['file']
        filePath = str(os.getenv('APP_DIR')) + uploadFile.name
        with open(filePath, 'wb+') as dest:
            for chunk in uploadFile.chunks():
                dest.write(chunk)

        try:
            metadata = aapt.get_apk_info(filePath)
        except Exception as e:
            return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)

        package = Package()
        package.application = filePath
        package.package_name = metadata['package_name']
        package.package_version_code = metadata['version_code']
        package.save()
        packageSerializer = PackageSerializer(package)
        return Response(packageSerializer.data, status = status.HTTP_201_CREATED)
