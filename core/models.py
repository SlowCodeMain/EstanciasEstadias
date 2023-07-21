from django.db import models

# Importacion de clases para creacion de usuario personalizado
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    AbstractUser
)


# Clase que hereda de BaseUserManager, BaseUserManager tiene los datos necesarios para la construccion
# de un usuario, es necesaria para crear una clase usuaria desde cero, es como el esquelo pricipal
class UsuarioBasePersonalizado(BaseUserManager):
    def create_user(self, email, password=None, **campos_extra):
        if not email:
            raise ValueError("El campo email no debe estar vacio")
        email = self.normalize_email(email)
        user = self.model(email=email, **campos_extra)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password=None, **campos_extra):
        campos_extra.setdefault('is_staff', True)
        campos_extra.setdefault('is_superuser', True)
        return self.create_user(email, password, **campos_extra)


# Esta clase sirve para agregar los campos necesarios para el modelo, Hace uso de dos clases:
#     AbstractBaseUser,
#     PermissionsMixin
# el primero nos permite agregar campos personalizados además de establecer el username field
# el segundo nor permite agregarle la funcionalidad de autenticacion
class UsuarioPersonalizado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, error_messages={'unique': 'Ya existe un usuario con ese correo'})
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=455)
    is_staff = models.BooleanField(default=False)
    tipo_usuario = models.CharField(max_length=20, choices=[('alumno', 'alumno'), ('empresa', 'empresa')])

    objects = UsuarioBasePersonalizado()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Alumno(UsuarioPersonalizado):
    matricula = models.CharField(max_length=6)
    carrera = models.CharField(max_length=50)
    aceptado = models.BooleanField(default=False)

    estancia_uno = models.BooleanField(default=False)
    estancia_dos = models.BooleanField(default=False)


class DetalleDireccionEmpresa(models.Model):
    entidad_federativa = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=70)
    codigo_postal = models.CharField(max_length=8)
    calle = models.CharField(max_length=70, null=True)


class DetalleContactoEmpresa(models.Model):
    numero_telefono_fijo = models.CharField(max_length=10)
    email = models.EmailField()
    celular = models.CharField(max_length=10)


class Empresa(UsuarioPersonalizado):
    nombre_empresa = models.CharField(max_length=200)
    irfc = models.CharField(max_length=20)
    carrera_aceptada = models.CharField(max_length=50)
    direccion_empresa = models.ForeignKey(DetalleDireccionEmpresa, on_delete=models.CASCADE)
    contacto = models.ForeignKey(DetalleContactoEmpresa, on_delete=models.CASCADE)


class Estancia(models.Model):
    tipo_estancia = models.CharField(max_length=15)
    cantidad_horas = models.IntegerField(default=120)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Estadia(models.Model):
    cantidad_horas = models.IntegerField(default=480)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
