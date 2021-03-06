from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Titulo(models.Model):    
    descripcion = models.CharField(verbose_name='Descricpion', max_length=300, unique=True)    
    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'        

    def __str__(self):
        return '{}'.format(self.descripcion)

class Provincia(models.Model):
    descripcion=models.CharField(verbose_name='Descripcion', max_length=100)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Provincia'
        verbose_name_plural='Provincias'
    def __str__(self):
        return '{}'.format(self.descripcion)
    
class Ciudad(models.Model):
    provincia=models.ForeignKey(Provincia, on_delete=models.PROTECT)
    descripcion=models.CharField(verbose_name='Descripcion', max_length=100)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Ciudad'
        verbose_name_plural='Ciudades'

    def __str__(self):
        return '{}'.format(self.descripcion)

class Profesion(models.Model):    
    descripcion=models.CharField(verbose_name='Descripcion', max_length=100, unique=True)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Profesion'
        verbose_name_plural='Profesiones'

    def __str__(self):
        return '{}'.format(self.descripcion)

class Persona(models.Model):
    tipo_sexo =(('N', 'Ninguno'), ('M', 'Masculino'), ('F', 'Femenino'))
    estado_civil=(('S', 'Soltero'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viudo'), ('U', 'Union Libre'))
    cedula=models.CharField('Cedula', max_length=13, unique=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombres')
    apellido=models.CharField(max_length=100, verbose_name='Apellidos')
    nacimiento=models.DateField('Fecha Nacimiento', blank=True, null=True)
    sexo=models.CharField('Sexo', choices=tipo_sexo, default='N', max_length=1)
    civil=models.CharField('Estado Civil', choices=estado_civil, default='S', max_length=1)
    profesion=models.ManyToManyField(Profesion)
    titulo=models.ManyToManyField(Titulo)
    provincia=models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad=models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    direccion=models.CharField('Direccion', max_length=100, blank=True, null=True)
    telefono=models.CharField('Telefono', max_length=100, blank=True, null=True)
    email=models.EmailField('Correo', max_length=100, blank=True, null=True)
    foto=models.ImageField('Foto', upload_to='fotos/', blank=True, null=True)

    class Meta:
        abstract=True

class Sangre(models.Model):    
    tipo=models.CharField(verbose_name='Tipo de Sangre', max_length=20, unique=True)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Tipo de Sangre'
        verbose_name_plural='Tipos de Sangre'

    def __str__(self):
        return '{}'.format(self.tipo)


class Paciente(Persona):
    sangre=models.ForeignKey(
        Sangre, on_delete=models.PROTECT, blank=True, null=True
    )
    hijos=models.IntegerField('No. hijos', default=0)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Paciente'
        verbose_name_plural='Pacientes'

    def __str__(self):
            return '{}'.format(self.nombre)

class Agenda(models.Model):
    paciente=models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha=models.DateField(
        'Fecha de Agenda', blank=True, null=True, default=now
    )
    hora=models.TimeField('Hora', default=now().date())
    motivo=models.CharField('Motivo de Consulta', max_length=100)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name='Agenda'
        verbose_name_plural='Agendas'

