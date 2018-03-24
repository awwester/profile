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

    # comma separated field
    tags = models.CharField(max_length=200, blank=True)

    @property
    def tag_list(self):
        """
        return a list of the tags from self.tags
        """
        return self.tags.split(',')

    def __str__(self):
        return self.title
