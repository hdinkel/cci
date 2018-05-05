from django.urls import path

from . import views

urlpatterns = (
    path('', views.AlertList.as_view(), name='alert_list'),
    path('new', views.AlertCreate.as_view(), name='alert_create'),
    path('{int:pk}', views.AlertUpdate.as_view(), name='alert_update'),
    path('{pk}/delete', views.AlertDelete.as_view(), name='alert_delete'),
    )
