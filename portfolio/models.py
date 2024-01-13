from django.db import models
from ckeditor.fields import RichTextField

class Header(models.Model):
    title = models.TextField()
    desc = models.TextField()
    file = models.FileField(upload_to='cv')
    image = models.FileField(upload_to='images')
    def __str__(self) -> str:
        return self.title

class ProfessionalBackground(models.Model):
    image = models.ImageField(upload_to='images')

class Service(models.Model):
    title = models.TextField()
    desc = models.TextField()
    color_code = models.CharField(max_length=255)
    background = models.ForeignKey(ProfessionalBackground,on_delete=models.CASCADE,related_name="services")
    def __str__(self) -> str:
        return self.title

class Skill(models.Model):
    image = models.ImageField(upload_to="images")
    title = models.TextField()
    color_code = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=2,decimal_places=1)
    def __str__(self) -> str:
        return self.title

class Project(models.Model):
    title = models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
    content = RichTextField()
    def __str__(self) -> str:
        return self.title

class Blog(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='images')
    desc = models.TextField(null=True,blank=True)
    content = RichTextField()
    duration = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to='images')

class Experience(models.Model):
    first = models.TextField()
    second = models.TextField()
    third = models.TextField()
    about_me = models.OneToOneField(AboutMe,on_delete=models.CASCADE,related_name="experience")

class CompleteProject(models.Model):
    first = models.TextField()
    second = models.TextField()
    third = models.TextField()
    about_me = models.OneToOneField(AboutMe,on_delete=models.CASCADE,related_name="complete_project")


class HappyCustomer(models.Model):
    first = models.TextField()
    second = models.TextField()
    third = models.TextField()
    about_me = models.OneToOneField(AboutMe,on_delete=models.CASCADE,related_name="happy_customer")
