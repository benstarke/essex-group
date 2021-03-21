from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class contact(models.Model):
    name  = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=False, blank=True)
    subject = models.CharField(max_length=255,null=False)
    message = models.TextField( null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    date_posted = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} - {self.author}"
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk':self.pk})
    class Meta:
        ordering = ('-date_posted',)

class Slider(models.Model):
    image = models.ImageField(upload_to='slides')