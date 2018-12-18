from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    short_description = models.TextField(default='Letters more than 200 will be sliced.')
    slug = models.SlugField(unique=True, default=False, blank=True)

    def save(self, *args, **kwargs):
        self.short_description = self.short_description[:200] + "...(continue reading)"
        self.slug = slugify(self.title[:49])
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
