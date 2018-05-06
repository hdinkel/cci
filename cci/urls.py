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
from django.conf.urls import url
from django.urls import path, include
from alerts import urls
from rest_framework import routers
from alerts import views
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'alerts', views.AlertViewSet)

schema_view = get_swagger_view(title='Alerts API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alerts/', include('alerts.urls')),
    url(r'^api/', include(router.urls), name='api'),
    url(r'^swagger$', schema_view, name='swagger')
    ]
