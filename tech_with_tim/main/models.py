from django.db import models


# Course
class Course(models.Model):
    course_name = models.CharField('Course name', max_length=255)
    description = models.CharField('Description', max_length=255)
    about = models.TextField('About')
    contact = models.CharField('Contact', max_length=255)
    image = models.ImageField('Choose image main (format: jpg, jpeg, png)')

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['-id']


# Teacher
class Teacher(models.Model):
    teacher_name = models.CharField('Teacher name', max_length=255)
    description = models.CharField('Description', max_length=255)
    about = models.TextField('About')
    contact = models.CharField('Contact', max_length=255)
    social_networks = models.CharField('Social networks', max_length=255)
    image = models.ImageField('Choose image main (format: jpg, jpeg, png)', upload_to='photo/%y/%m/%d')

    def __str__(self):
        return self.teacher_name

    class Meta:
        ordering = ['-id']


# Faq
class Faq(models.Model):
    question = models.CharField('Question', max_length=255)
    answer = models.CharField('Answer', max_length=255)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-id']


# Photo
class Photo(models.Model):
    photo = models.ImageField('Choose image main (format: jpg, jpeg, png)', upload_to='photo/%y/%m/%d')

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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


