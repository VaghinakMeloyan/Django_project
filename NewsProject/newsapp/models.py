from django.db import models


class Abstract(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(Abstract):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField('Url', unique=True)
    photo = models.ImageField(upload_to='newsapp/')

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField('Url', unique=True)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    add_category = models.ManyToManyField(Category, blank=True, related_name='news_add')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'





