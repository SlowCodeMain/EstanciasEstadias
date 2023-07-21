from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from core.models import Alumno, Empresa

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            # Redireccionar a diferentes paneles según el tipo de usuario
            if user.tipo_usuario == 'alumno':
                return redirect('home_alumno')  # Reemplaza 'alumno_panel' con el nombre de la URL para el panel de alumnos
            elif user.tipo_usuario == 'empresa':
                return redirect('home_empresa')  # Reemplaza 'empresa_panel' con el nombre de la URL para el panel de empresas
        else:
            error = 'Las credenciales no son válidas. Inténtalo de nuevo.'
            return render(request, 'home/login.html', {'error': error})

    return render(request, 'home/login.html')
