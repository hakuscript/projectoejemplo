from django.db import models

class Publicadore(models.Model):
  nombre = models.CharField(max_length=30)
  direccion = models.CharField(max_length=30)
  ciudad = models.CharField(max_length=50)
  pais = models.CharField(max_length=50)
  sitioWeb = models.CharField(max_length=50) 

  def __unicode__(self):
    return self.nombre
  
class Autore(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField()

  def __unicode__(self):
    return '%s %s'%(self.nombre,self.apellido)


class Libro(models.Model):
  titulo = models.CharField(max_length=100)
  autores = models.ManyToManyField(Autore)
  publicador = models.ForeignKey(Publicadore)
  fecha_publicacion = models.DateField()

  def __unicode__(self):
    return self.titulo
  
  
