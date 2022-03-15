from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.PackageView.as_view())
]
