from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import math

class Chunk(models.Model):
    part = models.CharField(max_length=100)
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    viewBox = models.CharField(max_length=30)
    image = models.ImageField()
    order_number = models.IntegerField()

    def __str__(self):
        return self.part

    def save(self, *args, **kwargs):
        self.slug=slugify(self.part)
        self.x_pos = self.x_pos - math.floor(self.width/2)
        self.y_pos = self.y_pos - math.floor(self.height/2)
        self.slug=slugify(self.part)
        super(Chunk, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mainMap:chunk', kwargs={'slug':self.slug})
        
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Lock(models.Model):
    name = models.CharField(max_length=100)
    chunk = models.ForeignKey(Chunk, related_name="lock", on_delete=models.CASCADE, blank=True, null = True)
    dimensions = models.CharField(max_length = 200)
    contact=models.CharField(max_length=200)
    distance=models.CharField(max_length=200)
    localization = models.CharField(max_length=30)
    state = models.BooleanField(default=True)
    image = models.ImageField()
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return slugify(self.name)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        pass

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Lock, self).save(*args, **kwargs)

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Marina(models.Model):
    name = models.CharField(max_length=100)
    chunk = models.ForeignKey(Chunk, related_name="marina", on_delete=models.CASCADE, blank=True, null = True)
    dimensions = models.CharField(max_length = 200)
    contact=models.CharField(max_length=200)
    distance=models.CharField(max_length=200)
    localization = models.CharField(max_length=30)
    state = models.BooleanField(default=True)
    image = models.ImageField()
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    meta = models.CharField(max_length=300, default="")

    def __str__(self):
        return slugify(self.name)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        pass

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Marina, self).save(*args, **kwargs)

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Weir(models.Model):
    name = models.CharField(max_length=100)
    chunk = models.ForeignKey(Chunk, related_name="weir", on_delete=models.CASCADE, blank=True, null = True)
    dimensions = models.CharField(max_length = 200)
    contact=models.CharField(max_length=200)
    distance=models.CharField(max_length=200)
    localization = models.CharField(max_length=30)
    state = models.BooleanField(default=True)
    image = models.ImageField()
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    meta = models.CharField(max_length=300, default="")

    def __str__(self):
        return slugify(self.name)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        pass

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Weir, self).save(*args, **kwargs)

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
