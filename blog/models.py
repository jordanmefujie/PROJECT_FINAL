from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.title

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    date_acquired = models.DateField()

    def __str__(self):
        return self.name

class ResearchLog(models.Model):
    experiment_name = models.CharField(max_length=200)
    researcher = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.experiment_name
