from django.contrib import admin
from .models import UsuarioPersonalizado, Empresa, Alumno, Estancia, Estadia

admin.site.register(UsuarioPersonalizado)
admin.site.register(Alumno)
admin.site.register(Empresa)
admin.site.register(Estancia)
admin.site.register(Estadia)


