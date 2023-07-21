from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from core.models import Alumno
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    if request.method == 'POST':
        pass
    return render(request, 'alumnos/home/home.html')

def registro(request):
    mensaje_exito = None
    error = None

    if request.method == 'POST':
        # Obtener los datos enviados por el formulario
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        matricula = request.POST.get('matricula')
        carrera = request.POST.get('carrera')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        tipo_usuario = 'alumno'

        # Verificar si las contraseñas coinciden
        if password != confirm_password:
            return render(request, 'alumnos/registro/registro.html', {'error': 'Las contraseñas no coinciden'})

        # Validar si ya existe un usuario con el mismo email
        if Alumno.objects.filter(email=email).exists():
            error = 'Ya existe un usuario con ese correo electrónico'
            return render(request, 'alumnos/registro/registro.html', {'exito': mensaje_exito, 'error': error})
        else:
            # Crear el alumno en la base de datos con contraseña hasheada
            hashed_password = make_password(password)
            alumno = Alumno.objects.create(
                email=email,
                password=hashed_password,
                nombre=nombre,
                apellidos=apellidos,
                telefono=telefono,
                direccion=direccion,
                matricula=matricula,
                carrera=carrera,
                tipo_usuario=tipo_usuario
            )
            mensaje_exito = f'¡El usuario {alumno.email} ha sido registrado exitosamente!'

    return render(request, 'alumnos/registro/registro.html', {'exito': mensaje_exito, 'error': error})
