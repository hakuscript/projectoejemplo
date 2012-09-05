from order.forms import ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMessage


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))



def contacto(request):
  if request.method=='POST':
      formulario = ContactoForm(request.POST)
      if formulario.is_valid():
          titulo = 'Este es un Mensaje de prueba =)'
          contenido = formulario.cleaned_data['mensaje'] + "\n"
          contenido+= 'Comunicarse a: '+ formulario.cleaned_data['correo']
          correo = EmailMessage(titulo, contenido, to=['gonzalo.bahamondez.c@gmail.com','arturo.tagle@biometrycloud.com'])
          correo.send()
          return HttpResponseRedirect('/')
  else:
    formulario = ContactoForm()
  return render_to_response('contactoform.html', {'formulario':formulario}, context_instance=RequestContext(request))
