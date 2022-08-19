from django.db import models
from django.utils.text import slugify


# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=255, null=False)
    SecondName = models.CharField(max_length=255, null=False)
    Registration = models.CharField(max_length=255, null=False)
    Hostel = models.BooleanField(null=False, default=False)
    LaptopSerialNumber = models.CharField(
        max_length=255, blank=True, default="No laptop"
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Student"

    def get_absolute_url(self):
        return "update/{slug}".format(slug=self.slug)

    def __str__(self):
        return self.FirstName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Registration)
        super(Student, self).save(*args, **kwargs)
