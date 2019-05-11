from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    begin_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    phone = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=None,null=True,blank=True)

    def __str__(self):
        return self.name