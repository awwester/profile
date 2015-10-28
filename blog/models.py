from django.db import models
from django.core.urlresolvers import reverse


class Tag(models.Model):
    "topic that an article is about"
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=50)
    headline = models.CharField(max_length=150)
    created = models.DateField(auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog-article', kwargs={'pk': self.id})

    def __str__(self):
        return self.title
