from rest_framework import serializers
from .models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['application', 'package_name', 'package_version_code']

class UploadSerializer(serializers.Serializer):
    uploadFile = serializers.FileField()
    class Meta:
        fields = ['file']
