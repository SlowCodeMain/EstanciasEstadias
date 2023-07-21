# Generated by Django 4.2.3 on 2023-07-21 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioPersonalizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(error_messages={'unique': 'Ya existe un usuario con ese correo'}, max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=455)),
                ('is_staff', models.BooleanField(default=False)),
                ('tipo_usuario', models.CharField(choices=[('alumno', 'alumno'), ('empresa', 'empresa')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleContactoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_telefono_fijo', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleDireccionEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad_federativa', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=70)),
                ('codigo_postal', models.CharField(max_length=8)),
                ('calle', models.CharField(max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('usuariopersonalizado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('matricula', models.CharField(max_length=6)),
                ('carrera', models.CharField(max_length=50)),
                ('aceptado', models.BooleanField(default=False)),
                ('estancia_uno', models.BooleanField(default=False)),
                ('estancia_dos', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuariopersonalizado',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('usuariopersonalizado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('irfc', models.CharField(max_length=20)),
                ('carrera_aceptada', models.CharField(max_length=50)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.detallecontactoempresa')),
                ('direccion_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.detalledireccionempresa')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuariopersonalizado',),
        ),
        migrations.CreateModel(
            name='Estancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_estancia', models.CharField(max_length=15)),
                ('cantidad_horas', models.IntegerField(default=120)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_horas', models.IntegerField(default=480)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresa')),
            ],
        ),
    ]
