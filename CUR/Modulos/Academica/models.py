from django.db import models

# Create your models here.


class Programa(models.Model):
    idPrograma = models.AutoField(primary_key=True)
    descripción = models.CharField(max_length=30)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.descripción)



class Facultad(models.Model):
    idFacultad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        txt = "{0} / Dirección: {1}"
        return txt.format(self.nombre, self.direccion)


class Carrera(models.Model):
    snies = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)
    modalidad = models.CharField(max_length=18)
    descripcion = models.CharField(max_length=120)
    tituloOtorgado = models.CharField(max_length=50)
    programa = models.ForeignKey(
        Programa, null=False, blank=False, on_delete=models.CASCADE
    )
    facultad = models.ForeignKey(
        Facultad, null=False, blank=False, on_delete=models.CASCADE
    )
    
    def __str__(self):
        txt = "{0} {1} {2} {3}"
        return txt.format(self.snies, self.nombre, self.duracion, self.modalidad)

class Estudiante(models.Model):
    numDocumento = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=35)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [("F", "Femenino"), ("M", "Masculino")]
    sexo = models.CharField(max_length=1, choices=sexos, default="F")
    carrera = models.ForeignKey(
        Carrera, null=False, blank=False, on_delete=models.CASCADE
    )
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0} {1} {2} {3} {4}"
        return txt.format(self.numDocumento ,self.nombres, self.apellidoPaterno, self.apellidoMaterno, self.fechaNacimiento)
    
    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)


class Docente(models.Model):
    numDocumento = models.CharField(max_length=18, primary_key=True)
    nombres = models.CharField(max_length=35)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    sexo = [("F", "Femenino"), ("M", "Masculino")]
    genero = models.CharField(max_length=1, choices=sexo, default="F")

    def __str__(self):
        txt = "{0} {1} {2}"
        return txt.format(self.numDocumento, self.nombres, self.apellidoPaterno, self.apellidoMaterno)


class Semestre(models.Model):
    idSemestre = models.AutoField(primary_key=True)
    descripción = models.CharField(max_length=30)
    totalCreditos = models.PositiveSmallIntegerField()

    def __str__(self):
        txt = "{0} / Creditos: {1}"
        return txt.format(self.descripción, self.totalCreditos)


class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(
        Docente, null=False, blank=False, on_delete=models.CASCADE
    )
    semestre = models.ForeignKey(
        Semestre, null=False, blank=False, on_delete=models.CASCADE
    )

    def __str__(self):
        txt = "{0} {1} {2}"
        return txt.format(self.codigo, self.nombre, self.docente)


class Matricula(models.Model):
    idMatricula = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante, null=False, blank=False, on_delete=models.CASCADE
    )
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3} "
        if self.estudiante.sexo =="F":
            letraSexo = "a"
        else:
            letraSexo = "o"

        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(),letraSexo, self.curso, fecMat)
