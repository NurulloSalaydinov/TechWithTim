from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required as staffonly
from django.http import JsonResponse
from django.db.models import Q
import json
from main.models import *
from .forms import *

@staffonly(login_url='/admin/login/')
def home(request):
    information = Information.objects.first()
    context = {
        'info': information
    }
    return render(request, 'tech_admin/index.html', context)


@staffonly(login_url='/admin/login/')
def course(request):
    key = request.GET.get('key')
    if key != None and key != '':
        result = Course.objects.filter(Q(course_name__contains=key) | Q(about__contains=key))
        if result.exists():
            info = f'Search results for 👉 {key}'
        else:
            info = 'Nothing Found 🤷‍♂️'
    else:
        info = ''
        result = Course.objects.filter(course_name='Empty')

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/courses/')
    else:
        form = CourseForm()

    courses = Course.objects.all()
    context = {
        'courses': courses,
        'form': form,
        'results': result,
        'key': info
    }
    return render(request, 'tech_admin/courses.html', context)

@staffonly(login_url='/admin/login/')
def teacher(request):
    key = request.GET.get('key')
    if key != None and key != '':
        result = Teacher.objects.filter(Q(teacher_name__contains=key) | Q(about__contains=key))
        if result.exists():
            info = f'Search results for 👉 {key}'
        else:
            info = 'Nothing Found 🤷‍♂️'
    else:
        info = ''
        result = Course.objects.filter(course_name='Empty')

    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/teachers/')
    else:
        form = TeacherForm()

    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
        'form': form,
        'results': result,
        'key': info
    }
    return render(request, 'tech_admin/teachers.html', context)

@staffonly(login_url='/admin/login/')
def faq(request):
    key = request.GET.get('key')
    if key != None and key != '':
        result = Faq.objects.filter(Q(question__contains=key) | Q(answer__contains=key))
        if result.exists():
            info = f'Search results for 👉 {key}'
        else:
            info = 'Nothing Found 🤷‍♂️'
    else:
        info = ''
        result = Course.objects.filter(course_name='Empty')

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/faqs/')
    else:
        form = FaqForm()

    faq = Faq.objects.all()
    context = {
        'faqs': faq,
        'form': form,
        'results': result,
        'key': info
    }
    return render(request, 'tech_admin/faq.html', context)

@staffonly(login_url='/admin/login/')
def gallery(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/galleries/')
    else:
        form = PhotoForm()

    photo = Photo.objects.all()
    context = {
        'photos': photo,
        'form': form,
    }
    return render(request, 'tech_admin/gallery.html', context)

@staffonly(login_url='/admin/login/')
def contact(request):
    key = request.GET.get('key')
    if key != None and key != '':
        result = Contact.objects.filter(Q(name__contains=key) | Q(surname__contains=key))
        if result.exists():
            info = f'Search results for 👉 {key}'
        else:
            info = 'Nothing Found 🤷‍♂️'
    else:
        info = ''
        result = Course.objects.filter(course_name='Empty')

    contacts = Contact.objects.filter(is_pinned=False)
    pinnedcontacts = Contact.objects.filter(is_pinned=True)
    context = {
        'contacts': contacts,
        'pinneds': pinnedcontacts,
        'results': result,
        'key': info
    }
    return render(request, 'tech_admin/contact.html', context)

@staffonly(login_url='/admin/login/')
def settings(request):
    setting = Settings.objects.first()
    if request.method == 'POST':
        form = SettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('/admin/settings/')
    else:
        form = SettingForm(instance=setting)
    context = {
        'form': form,
        'obj': setting
    }
    return render(request, 'tech_admin/settings.html', context)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
    return render(request, 'tech_admin/login.html')

def admin_logout(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'tech_admin/logout.html')
    return render(request, 'tech_admin/logout.html')

def set_false(request):
    info = Information.objects.first()
    info.is_new = False
    info.save()
    return JsonResponse({'success': 200})

# def search(request):
#     key = request.GET.get('key')
#     if key == None:
#         key = ''
#     course = Course.objects.filter(Q(course_name__contains=f'{key}'))
#     teacher = Teacher.objects.filter(Q(teacher_name__contains=f'{key}'))
#     faq = Faq.objects.filter(Q(question__contains=f'{key}') | Q(answer__contains=f'{key}'))
#     photo = Photo.objects.filter(photo__contains=f'{key}')
#     contact = Contact.objects.filter(name__contains=f'{key}')
#     context = {
#         'courses': course,
#         'teachers': teacher,
#         'faqs': faq,
#         'photos': photo,
#         'key': key
#     }
#     return render(request, 'tech_admin/search.html', context)

# course extra functions
@staffonly(login_url='/admin/login/')
def coursedelete(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == 'POST' and course:
        course.delete()
        return redirect('/admin/')
    return render(request, 'tech_admin/delete.html', {'obj': course})

@staffonly(login_url='/admin/login/')
def courseedit(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = CourseForm(instance=course)

    return render(request, 'tech_admin/update.html', {'form': form})


# teacher extra functions
@staffonly(login_url='/admin/login/')
def teacherdelete(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST' and teacher:
        teacher.delete()
        return redirect('/admin/')
    return render(request, 'tech_admin/delete.html', {'obj': teacher})

@staffonly(login_url='/admin/login/')
def teacheredit(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'tech_admin/update.html', {'form': form})


# faq extra functions
@staffonly(login_url='/admin/login/')
def faqdelete(request, pk):
    faq = get_object_or_404(Faq, id=pk)
    if request.method == 'POST' and faq:
        faq.delete()
        return redirect('/admin/')
    return render(request, 'tech_admin/delete.html', {'obj': faq})

@staffonly(login_url='/admin/login/')
def faqedit(request, pk):
    faq = get_object_or_404(Faq, id=pk)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = FaqForm(instance=faq)

    return render(request, 'tech_admin/update.html', {'form': form})


# gallery extra functions
@staffonly(login_url='/admin/login/')
def gallerydelete(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    if request.method == 'POST' and photo:
        photo.delete()
        return redirect('/admin/')
    return render(request, 'tech_admin/delete.html', {'obj': photo})

@staffonly(login_url='/admin/login/')
def galleryedit(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = PhotoForm(instance=photo)

    return render(request, 'tech_admin/update.html', {'form': form})

# contact
@staffonly(login_url='/admin/login/')
def contactpin(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    if contact.is_pinned:
        contact.is_pinned = False
        contact.save()
        return redirect('/admin/contacts/')
    else:
        contact.is_pinned = True
        contact.save()
        return redirect('/admin/contacts/')

@staffonly(login_url='/admin/login/')
def contactdelete(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    if request.method == 'POST' and contact:
        contact.delete()
        return redirect('/admin/contacts/')
    return render(request, 'tech_admin/delete.html', {'obj': contact})