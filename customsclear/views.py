from django.core.mail import send_mail, BadHeaderError
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import Service, About, Employee, Client, GalleryImage, SpecialisedItem
from .forms import ContactForm

# Create your views here.


def home(request):
    service = Service.objects
    about = About.objects.get(pk=1)
    employee = Employee.objects
    client = Client.objects
    gallery = GalleryImage.objects
    item = SpecialisedItem.objects


    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, 'home.html', {'service': service, 'about': about, 'employee': employee, 'gallery': gallery, 'client': client, 'item': item, 'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
