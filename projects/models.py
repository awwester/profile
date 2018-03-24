from django.db import models

class Project(models.Model):
    """
    individual projects that I have worked on
    """

    title = models.CharField(max_length=50)
    url = models.URLField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='projects/')
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title
