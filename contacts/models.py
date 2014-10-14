from django.db import models

# Create your models here.
class Contact(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_last_modified = models.DateTimeField(auto_now_add=True)

    industry = models.ManyToManyField('Industry')
    type = models.ManyToManyField('Type')

    name = models.CharField(max_length=30)

    address = models.TextField()
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Industry(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_last_modified = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Type(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_last_modified = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name