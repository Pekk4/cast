from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ConsultantAPIView, TechAPIView, ImportCertificatesView, CertAPIView, ProjectAPIView
from core.decorators import token_required


router = routers.DefaultRouter()
router.register(r'consultant', ConsultantAPIView, basename='consultant')

consultant_list = ConsultantAPIView.as_view({
    'get': 'list',
    'post': 'create'
})
consultant_detail = ConsultantAPIView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

tech_list = TechAPIView.as_view({
    'get': 'list',
    'post': 'get_or_create'
})

tech_detail = TechAPIView.as_view({
    'get': 'retrieve',
    'post': 'create'
})

cert_list = CertAPIView.as_view({
    'get': 'list',
    'post': 'create'
})

project_list = ProjectAPIView.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    path('consultant/', token_required(consultant_list), name='consultant-list'),
    path('consultant/<int:pk>/', consultant_detail, name='consultant-detail'),
    path('tech/', tech_list, name='tech-list'),
    path('tech/<int:pk>', tech_detail, name='tech-detail'),
    path('certificates/', cert_list, name='cert-list'),
    path('import-certificates/', ImportCertificatesView.as_view(), name='upload-file'),
    path('projects/', project_list, name='project-list'),
])
