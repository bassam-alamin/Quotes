from django.db import models
from django.urls import reverse

class Author(models.Model):
    author = models.CharField(max_length=100)
    author_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('upload:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.author

class Saying(models.Model):
    speaker = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse('upload:detail',kwargs={'pk':self.speaker_id})


    def __str__(self):

        return self.category
