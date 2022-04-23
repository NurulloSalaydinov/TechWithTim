from django.db import models
from django_resized import ResizedImageField
import uuid


# Home Page Informations for Admin Panel
class Information(models.Model):
    visitors = models.IntegerField('Visitors', default=0)
    visits = models.IntegerField('Visits', default=0)
    registerated = models.IntegerField('Registerated', default=0)
    is_new = models.BooleanField('Is New', default=False)

    def __str__(self):
        return f"Visitors: {self.visitors}, Visits: {self.visits}, Registerated: {self.registerated}"


# Course
class Course(models.Model):
    course_name = models.CharField('Course name', max_length=255)
    about = models.TextField('About')
    image = ResizedImageField('Choose image main (format: jpg, jpeg, png)', size=[400, 350], crop=['middle', 'center'], force_format='PNG', quality=100)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['-id']


# Teacher
class Teacher(models.Model):
    teacher_name = models.CharField('Teacher name', max_length=255)
    about = models.TextField('About')
    facebook = models.CharField('@Facebook', max_length=255)
    instagram = models.CharField('@Instagram', max_length=255)
    twitter = models.CharField('@Twitter', max_length=255)
    image = ResizedImageField('Choose image main (format: jpg, jpeg, png)', size=[400, 350], crop=['middle', 'center'], force_format='PNG', quality=100)

    def __str__(self):
        return self.teacher_name

    class Meta:
        ordering = ['-id']


# Faq
class Faq(models.Model):
    question = models.CharField('Question', max_length=255)
    answer = models.CharField('Answer', max_length=655)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-id']


# Photo
class Photo(models.Model):
    photo = ResizedImageField('Choose image main (format: jpg, jpeg, png)', size=[800, 600], crop=['middle', 'center'], force_format='PNG', quality=100)

    def __str__(self):
        return f'Photo {self.photo}'

    class Meta:
        ordering = ['-id']


# Contact
class Contact(models.Model):
    name = models.CharField('Name', max_length=255)
    surname = models.CharField('Surname', max_length=255)
    phone = models.CharField('Phone', max_length=255)
    theme = models.CharField('Theme', max_length=255)
    message = models.TextField('Message')
    created_at = models.DateTimeField('Time', auto_now_add=True)
    is_pinned = models.BooleanField('Pin', default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


# Settings
class Settings(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    facebook = models.CharField('@Facebook', max_length=255)
    youtube = models.CharField('@Youtube', max_length=255)
    instagram = models.CharField('@Instagram', max_length=255)
    telegram = models.CharField('@Telegram', max_length=255)

    def __str__(self):
        return self.email

