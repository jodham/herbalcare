from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Herbalist(models.Model):
    HerbalistId = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=30)
    HerbalistLname = models.CharField(max_length=30)
    HerbalistUsername = models.CharField(max_length=20)
    herbalistEmail = models.EmailField()
    HerbalistContact = models.CharField(max_length=15)
    HerbalistSpecialization = models.CharField(max_length=255)

    def __str__(self):
        return self.FirstName


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profilepics')

    def __str__(self):
        return f'{self.user.username} profile'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post_detail', kwargs={'pk': self.pk})


class DiseaseStatus(models.Model):
    statusId = models.AutoField(primary_key=True, max_length=5)
    statusDescription = models.CharField(max_length=100)

    def __str__(self):
        return self.statusDescription


class Disease(models.Model):
    DiseaseName = models.CharField(max_length=50)
    DiseaseDescription = models.TextField()
    status = models.ForeignKey(DiseaseStatus, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    DiseasePhoto = models.ImageField(default="default.jpeg", upload_to='diseasePhotos')

    def __str__(self):
        return self.DiseaseName

    def get_absolute_url(self):
        return reverse('Disease_detail', kwargs={'pk': self.pk})


class Herb(models.Model):
    HerbId = models.AutoField(primary_key=True)
    HerbName = models.CharField(max_length=40)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    HerbPhoto = models.ImageField(default="default.jpeg", upload_to='HerbPhotos')
    diseaseName = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return self.HerbName
