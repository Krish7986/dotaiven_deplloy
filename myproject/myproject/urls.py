"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from avien_deploy.views import re,user_profile
from app2.views import home,product
from mixin1.views import viewers
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app2.urls')),
    path("mix/",viewers.as_view())
    
    # path("re/",re),
    # path("profile/",user_profile),
    # path("name/",name),
    # path("product/<int:id>",product)
]
