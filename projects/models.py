from django.db import models

class Project(models.Model):
    """
    individual projects that I have worked on
    """

    title = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='projects/')
    hidden = models.BooleanField(default=False)

    # determine the order the projects should be shown
    order = models.IntegerField(default=0)

    # comma separated field
    tags = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['order']

    @property
    def tag_list(self):
        """
        return a list of the tags from self.tags
        """
        return self.tags.split(',')

    def __str__(self):
        return self.title
