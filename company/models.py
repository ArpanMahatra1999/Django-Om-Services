from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='article_images/')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image: {self.image.name}"
