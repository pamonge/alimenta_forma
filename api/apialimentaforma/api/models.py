from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# TIPOS DE USUARIO ---------------------------------------------

class UserType (models.Model):
  categoryChoices = (
    ('c', 'empresa'),
    ('p', 'profesor'),
    ('s', 'estudiante'),
    ('a', 'administrador')
  )
  category = models.CharField(max_length=1, choices= categoryChoices, default= 's', verbose_name= 'Categoria')

  def __str__(self):
    return self.category
  
  class Meta:
    verbose_name= 'Categoria'
    verbose_name_plural= 'Categorias'

# PERFIL DE CADA USUARIO -----------------------------------------

class Profile (models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile', verbose_name= 'Usuario')
  location = models.CharField(max_length=150, verbose_name= 'Ciudad')
  image = models.ImageField(default='defaultUser.png', upload_to='user/', verbose_name= 'Imagen')
  phone = models.CharField(max_length= 15, verbose_name= 'Telefono')
  description = models.CharField(max_length= 500, verbose_name= 'Descripcion')
  userType = models.ForeignKey(UserType, on_delete= models.CASCADE, verbose_name= 'Categoria')
  cv = models.FileField(upload_to='user/',blank= True, null=True, verbose_name= 'CV')

  def __str__(self):
    return self.user.username

  class Meta:
    verbose_name = 'perfil'
    verbose_name_plural = 'perfiles'
    ordering = ['-id']

def create_user_profile (sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile (sender, instance, **Kwargs):
    instance.profile.save()
    
post_save.connect (create_user_profile, sender=User)
post_save.connect (save_user_profile, sender=User)

# TIPOS DE MEMBRESIA QUE PUEDE HABER -------------------------------------

class Offer (models.Model):
  price = models.IntegerField(verbose_name= 'Precio')
  detail = models.CharField(max_length= 500, verbose_name= 'Detalle')
  userType = models.ForeignKey(UserType, on_delete= models.CASCADE, verbose_name= 'Categoria')

  def __str__(self):
    return self.userType.category

  class Meta:
    verbose_name = 'Membresia'
    verbose_name_plural = 'Membresias'

# ANUNCIOS DE LOS MIEMBROS, RESERVADO PARA EMPRESAS --------------------------------

class Announcement (models.Model):
  detail =  models.FileField(upload_to='Announcement/', verbose_name = 'Detalle')
  owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')

  def __str__(self):
    return self.title

  class Meta:  
    verbose_name = 'Anuncio'
    verbose_name_plural = 'Anuncios'

# CONTENIDO DE LOS CURSOS, ESTO SE GENERA SI SE REQUIERE ---------------------------------

class Content (models.Model):
  title = models.CharField(max_length=150, verbose_name= 'Tutulo')
  comment = models.CharField(max_length=500, verbose_name= 'Comentario')
  img = models.ImageField(upload_to='material/', blank= True, null= True , verbose_name= 'Material grafico')
  doc = models.FileField(upload_to='material/', blank= True, null= True , verbose_name= 'Material escrito')
  videos = models.FileField(upload_to='material/', blank= True, null= True , verbose_name= 'Material de video')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Contenido'
    verbose_name_plural = 'Contenidos'

# CURSOS DISPONIBLES, LOS COLOCAN LOS PROFESORES ---------------------------------------------

class Course (models.Model):
  statusChoices = (
    ('i', 'inscripción'),
    ('d', 'desarrollo'),
    ('f', 'finalizado'),
  )

  title = models.CharField(max_length=150, verbose_name= 'Titulo')
  detail = models.CharField(max_length=500, verbose_name = 'Detalle')
  classes = models.IntegerField(verbose_name= 'Clases')
  teacher = models.ForeignKey(User, verbose_name= 'Profesor', on_delete=models.CASCADE)
  status = models.CharField(max_length=1, choices= statusChoices, default= 'i', verbose_name= 'Estado')
  content = models.ForeignKey(Content, on_delete=models.CASCADE, blank= True, null=True, verbose_name='Contenido')

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'Curso'
    verbose_name_plural = 'Cursos'

# REGISTRO DE USUARIOS ----------------------------------------

class Registration (models.Model):
  course = models.ForeignKey(Course, on_delete= models.CASCADE, verbose_name= 'Curso')
  student = models.ForeignKey(User, related_name= 'student_registration', on_delete= models.CASCADE, verbose_name= 'Alumno')
  enabled = models.BooleanField(default= True, verbose_name= 'Alumno regular')

  def __str__(self):
    return f'{self.student.username} - {self.course.title}'
  
  class Meta:
    verbose_name: 'Inscripción'
    verbose_name_plural = 'Inscripciones'

# ASISTENCIAS A LOS CURSOS ------------------------------------------

class Attendance (models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name= 'Curso')
  student = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'attendance', verbose_name= 'Alumno')
  date = models.DateField(null= True, blank=True, verbose_name='Fecha')
  present = models.BooleanField(default= False, blank=True, null=True, verbose_name= 'Presente')

  def __str__(self):
    return f'Asistencia - {self.id}'

  def updateRegistrationEnabledStatus (self):
    courseInstance = Course.objects.get(id=self.course.id)
    totalClasses = courseInstance.classes
    totalAbsences = Attendance.objects.filter(student=self.student, course=self.course, present=False).count()
    absencesPercent = (totalAbsences / totalClasses) * 100
    
    registration = Registration.objects.get(course=self.course, student=self.student)
    
    if absencesPercent > 20:
      registration.enabled = False
    else:
      registration.enabled = True
    
    registration.save()
    
  class Meta:
    verbose_name = 'Asistencia'
    verbose_name_plural = 'Asistencias'

# CALIFICACIONES DE LOS CURSOS EN LOS CURSOS -----------------------------------

class Mark (models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
  student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'estudiantes'}, verbose_name='Estudiante')
  mark_1 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 1')
  mark_2 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 2')
  mark_3 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 3')
  average = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='Promedio')
  
  def __str__(self):
    return str(self.course)
  
  # Calcular el promedio de las notas
  def calculate_average (self):
    marks = [self.mark_1, self.mark_2, self.mark_3]
    valid_marks = [mark for mark in marks if mark is not None]
    if valid_marks:
      return sum(valid_marks) / len (valid_marks)
    return None
  
  def save (self, *args, **kwargs):
    if self.mark_1 or self.mark_2 or self.mark_3:
      self.average = self.calculate_average()
    super().save(*args, **kwargs)
      
  class Meta:
    verbose_name = 'Nota'
    verbose_name_plural = 'Notas'