from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from core.models import Alumno, Empresa, DetalleDireccionEmpresa, DetalleContactoEmpresa


def home(request):
    if request.method == 'POST':
        pass
    return render(request, 'empresas/home/home.html')


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
        irfc = request.POST.get('irfc')
        carrera_aceptada = request.POST.get('carrera_aceptada')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        nombre_empresa = request.POST.get('nombre_empresa')
        tipo_usuario = 'empresa'

        # Verificar si las contraseñas coinciden
        if password != confirm_password:
            return render(request, 'empresas/registro/registro.html', {'error': 'Las contraseñas no coinciden'})

        # Validar si ya existe una empresa con el mismo email
        if Empresa.objects.filter(email=email).exists():
            error = 'Ya existe una empresa con ese correo electrónico'
            return render(request, 'empresas/registro/registro.html', {'exito': mensaje_exito, 'error': error})

        else:
            # Crear la empresa en la base de datos con contraseña hasheada
            hashed_password = make_password(password)

            # Crear detalles de dirección y contacto para la empresa
            entidad_federativa = request.POST.get('entidad_federativa')
            ciudad = request.POST.get('ciudad')
            codigo_postal = request.POST.get('codigo_postal')
            calle = request.POST.get('calle')
            numero_telefono_fijo = request.POST.get('numero_telefono_fijo')
            email_contacto = request.POST.get('email_contacto')
            celular = request.POST.get('celular')

            direccion_empresa = DetalleDireccionEmpresa.objects.create(
                entidad_federativa=entidad_federativa,
                ciudad=ciudad,
                codigo_postal=codigo_postal,
                calle=calle,
            )

            contacto_empresa = DetalleContactoEmpresa.objects.create(
                numero_telefono_fijo=numero_telefono_fijo,
                email=email_contacto,
                celular=celular,
            )

            empresa = Empresa.objects.create(
                nombre=nombre,
                email=email,
                password=hashed_password,
                nombre_empresa=nombre_empresa,
                apellidos=apellidos,
                telefono=telefono,
                direccion=direccion,
                irfc=irfc,
                carrera_aceptada=carrera_aceptada,
                direccion_empresa=direccion_empresa,
                contacto=contacto_empresa,
                tipo_usuario=tipo_usuario
            )
            mensaje_exito = f'¡La empresa {empresa.nombre_empresa} ha sido registrada exitosamente!'

    return render(request, 'empresas/registro/registro.html', {'exito': mensaje_exito, 'error': error})
