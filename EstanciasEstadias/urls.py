
from django.contrib import admin
from django.urls import path, include

from alumnos import urls as urls_alumnos
from empresas import urls as urls_empresas
from home import urls as urls_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumno/', include(urls_alumnos)),
    path('empresa/', include(urls_empresas)),
    path('home/', include(urls_home)),
]
