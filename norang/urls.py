"""norang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from unknownstation.views import MyLoginView
from unknownstation import views as unknownstationView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('blog/' ,include('unknownstation.urls')),
    re_path(r'^markdownx/', include('markdownx.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', MyLoginView.as_view(template_name='registration/login.html'), name="mylogin"),
    path('', unknownstationView.home, name='home' )
]
