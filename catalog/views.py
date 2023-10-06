from django.shortcuts import render, redirect
from .models import Mailing

# Create your views here.


def index(request):
    mailings = Mailing.objects.all()
    return render(request, 'index.html', {'mailings': mailings})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        audience = request.POST['audience']

        mailing = Mailing(title=title, text=text, audience=audience)
        mailing.save()
        return redirect('index')

    return render(request, 'create.html')

def update(request, id):
    mailing = Mailing.objects.get(pk=id)
    if request.method == 'POST':
        mailing.title = request.POST['title']
        mailing.text = request.POST['text']
        mailing.audience = request.POST['audience']

        mailing.save()
        return redirect('index')

    return render(request, 'update.html', {'mailing': mailing})

def delete(request, id):
    mailing = Mailing.objects.get(pk=id)
    mailing.delete()
    return redirect('index')

