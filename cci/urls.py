"""cci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from alerts import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'alerts', views.AlertViewSet)

SCHEMA_VIEW = get_swagger_view(title='Alerts API')

urlpatterns = [
    path('', views.AlertList.as_view(), name='alert_list'),
    path('alerts/', include('alerts.urls')),
    path('api/', include(ROUTER.urls), name='api'),
    path('swagger/', SCHEMA_VIEW, name='swagger'),
    path('admin/', admin.site.urls),
    ]
