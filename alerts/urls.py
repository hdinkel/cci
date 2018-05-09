"""
main urls.py for project
"""
from django.urls import path
from . import views

# TODO: urlpatterns
urlpatterns = (
    path('', views.AlertList.as_view(), name='alert_list'),
    path('new', views.AlertCreate.as_view(), name='alert_create'),
    path('<int:pk>', views.AlertUpdate.as_view(), name='alert_update'),
    path('<int:pk>/delete', views.AlertDelete.as_view(), name='alert_delete'),)
