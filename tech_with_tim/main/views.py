from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm

def gallery(req):
    photo = Photo.objects.all()
    context = {
        'photos': photo
    }
    return render(req, 'core/gallery.html', context)

def teachers(req):
    teacher = Teacher.objects.all()
    context = {
        'teachers': teacher
    }
    return render(req, 'core/teachers.html', context)

def home(request):
    course = Course.objects.all()
    teacher = Teacher.objects.all()
    faq = Faq.objects.all()
    photo = Photo.objects.all()
    info = Information.objects.first()
    if 'is_new' in request.session:
        print('This user have entered before')
    else:
        info.visitors += 1
        info.is_new = True
        info.save()
        request.session['is_new'] = False
    if request.session['is_new']:
        info.visitors += 1
        info.is_new = True
        info.save()
        request.session['is_new'] = False
    else:
        info.visits += 1
        info.is_new = True
        info.save()
        request.session['is_visitor'] = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            info.is_new = True
            info.registerated += 1
            info.save()
            return redirect('/')
    else:
        form = ContactForm()
    context = {
        'courses': course,
        'teachers': teacher,
        'faqs': faq,
        'photos': photo,
        'form': form
    }
    return render(request, 'core/index.html', context)
