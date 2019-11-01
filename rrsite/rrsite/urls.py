"""rrsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from mainapp import views as mainapp_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', mainapp_views.index, name='home'),
    path("about/", mainapp_views.about, name='about'),
    path("portfolio/", mainapp_views.portfolio, name='portfolio'),
    path("socials/", mainapp_views.socials, name='socials'),
    path("contact/", mainapp_views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()