"""
URL configuration for config project.

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
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 1. Ruta para el panel de administración
    path('admin/', admin.site.urls),

    # 2. Ruta para el login (asegurándonos que busque el template correcto)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # 3. Ruta para el resto de tu aplicación (home, juegos, perfil)
    path('', include('core.urls')),
]
