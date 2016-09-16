from django.db import models
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class SlugManager(models.Manager):
    def filter_slug(self, *args):
        return self.filter(slug=args[0])


class SaveSlugTitle(models.Model):
    "set the slug based on the title field"

    slug = models.SlugField(db_index=True, unique=True,
        editable=False, blank=True)
    objects = SlugManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(SaveSlugTitle, self).save(*args, **kwargs)


class Tag(models.Model):
    "topic that an article is about"
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(SaveSlugTitle):
    title = models.CharField(max_length=50)
    headline = models.CharField(max_length=150)
    created = models.DateField(auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    series = models.ForeignKey(Series, null=True, blank=True)
    public = models.BooleanField(default=True)
    video_id = models.CharField(max_length=15, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    """
    show_article_section will determine if the article is shown on the main
    blog articles page.
    """
    show_article_section = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-article', kwargs={'slug': self.slug})

    def record_view(self):
        """
        keep track of how many times an article has been viewed
        """
        self.view_count = self.view_count + 1
        self.save()

    def title_with_series(self):
        if self.series:
            series_title = self.series.title
            return self.title.replace(series_title + " ", "")
        else:
            return self.title

    def get_related_article(self):
        potential_articles = Article.objects.exclude(id=self.id)

        return potential_articles.order_by('?').first()

    def get_image_path(self):
        tag_titles = []
        tags = self.tags.all()

        for t in tags:
            tag_titles.append(t.title)

        if 'Django' in tag_titles:
            return static('img/topics/django.png')
        elif 'Ember' in tag_titles:
            return static('img/topics/ember.png')
        elif 'Angular' in tag_titles:
            return static('img/topics/angular.jpg')

    def series_previous(self):
        "return the previous article in the series or None"
        if self.series:
            series_articles_qs = Article.objects.filter(series=self.series)
            series_article_index = list(series_articles_qs).index(self)

            if series_article_index < len(series_articles_qs) - 1:
                return series_articles_qs[series_article_index + 1]

        return None

    def series_next(self):
        "return the next article in the series or None"
        if self.series:
            series_articles_qs = Article.objects.filter(series=self.series)
            series_article_index = list(series_articles_qs).index(self)

            if series_article_index > 0:
                return series_articles_qs[series_article_index - 1]

        return None
