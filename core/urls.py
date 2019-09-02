from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('apps/', views.app_index, name='app_index'),
    path('apps/create/', views.app_create, name='app_create'),
    path('apps/<int:app_id>/', views.app_details, name='app_details'),
    path('apps/<int:app_id>/edit/', views.app_create, name='app_edit'),
    path('apps/<int:app_id>/delete/', views.app_delete, name='app_delete'),
    path('apps/<int:app_id>/keys/create/', views.key_create, name='key_create_app'),
    path('keys/', views.key_index, name='key_index'),
    path('keys/create/', views.key_create, name='key_create'),
    path('keys/<int:key_id>/details/', views.key_details, name='key_details'),
    path('keys/<int:key_id>/edit/', views.key_create, name='key_edit'),
    path('keys/<int:key_id>/delete/', views.key_delete, name='key_delete'),
    path('log/', views.audit_log, name='audit_log'),
    path('api/check/', views.api_check, name='api_check'),
    path('api/activate/', views.api_activate, name='api_activate'),
    path('api/bulk-key-create/', views.api_bulk_key_create, name='api_bulk_key_create'),
]
