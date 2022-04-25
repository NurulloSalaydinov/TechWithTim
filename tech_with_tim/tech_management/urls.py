from django.urls import path
from .import views

app_name = 'tech'

urlpatterns = [
    path('', views.home, name="home"),
    path('courses/', views.course, name="course"),
    path('teachers/', views.teacher, name="teacher"),
    path('faqs/', views.faq, name="faq"),
    path('galleries/', views.gallery, name="gallery"),
    path('contacts/', views.contact, name="contact"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.admin_login, name="login"),
    path('logout/', views.admin_logout, name="logout"),
    path('set_false/', views.set_false, name="set_false"),
    # path('search/', views.search, name='search'),


    path('courses/edit/<int:pk>/', views.courseedit, name="course_edit"),
    path('courses/delete/<int:pk>/', views.coursedelete, name="course_delete"),

    path('teachers/edit/<int:pk>/', views.teacheredit, name="teacher_edit"),
    path('teachers/delete/<int:pk>/', views.teacherdelete, name="teacher_delete"),

    path('faqs/edit/<int:pk>/', views.faqedit, name="faq_edit"),
    path('faqs/delete/<int:pk>/', views.faqdelete, name="faq_delete"),

    path('galleries/edit/<int:pk>/', views.galleryedit, name="gallery_edit"),
    path('galleries/delete/<int:pk>/', views.gallerydelete, name="gallery_delete"),

    path('contacts/pin/<int:pk>/', views.contactpin, name="contact_pin"),
    path('contacts/delete/<int:pk>/', views.contactdelete, name="contact_delete"),


]
