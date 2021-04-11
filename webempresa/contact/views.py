from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm 

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            email = EmailMessage(
            "La caffetiera: Nuevo mensaje de contacto",
            "De {} <{}> \n escribió: \n \n {} ".format(name, email, content),
            "no-responder@gmail.com",
            ["tomiapi@hotmail.com"],
            reply_to=[email]  
            ) 
        try:
            email.send()
        #Si todo fue bien
            return redirect(reverse('contact')+'?ok')
        except:
        #Si hubo un fallo
            return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html',{'form':contact_form})
