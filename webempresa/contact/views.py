from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
# Create your views here.
def contact(request):
    contact_form = ContactForm() # Instancia del formulario

    if request.method == "POST": # Si el metodo es POST
        contact_form = ContactForm(data=request.POST) # Instancia del formulario con los datos
        if contact_form.is_valid(): # Si el formulario es valido
            name = request.POST.get('name', '') # Obtenemos el nombre
            email = request.POST.get('email', '') # Obtenemos el email
            message = request.POST.get('message', '') # Obtenemos el mensaje

            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", # Asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, message), # Cuerpo
                "no-contestar@inbox.mailtrap.io", # Email origen
                ["jcadcurso@gmail.com"], # Email destino
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'form':contact_form})