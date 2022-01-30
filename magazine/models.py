from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    # Personal data
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=True, null=True)
    # Description
    short_intro1 = models.CharField(verbose_name=_('Descriere scurta 1'), max_length=200, blank=True, null=True)
    short_intro2 = models.CharField(verbose_name=_('Descriere scurta 2'), max_length=200, blank=True, null=True)
    bio = models.TextField(verbose_name=_('Sinopsis'), blank=True, null=True)
    profile_image = models.ImageField(
        verbose_name=_('Profile Image'),
        upload_to='images/',
        default='images/default.png',
        null=True, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return str(self.name)


class Magazine(models.Model):
    title = models.CharField(verbose_name=_('Titlu'), max_length=200, blank=True, null=True)
    number = models.CharField(verbose_name=_('Număr Revistă'), max_length=200, blank=True, null=True)
    publish_year = models.CharField(verbose_name=_('Anul publicării'), max_length=200, blank=True, null=True)
    description = models.TextField(verbose_name=_('Sinopsis'), null=True, blank=True)
    url = models.CharField(verbose_name=_('Google Drive Link'), max_length=200, blank=True, null=True)
    featured = models.BooleanField(verbose_name=_('Prima Pagina'), max_length=200, default=False)
    slug = models.SlugField(
        default='',
        max_length=200,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Magazine"
        verbose_name_plural = "Magazines"
        ordering = ('publish_year',)

    def get_absolute_url(self):
        return reverse("magazine:pdf_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        value = self.title + '-' + self.number + '-' + self.publish_year
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name=_('Titlu'), max_length=200, blank=True, null=True)
    description = models.TextField(verbose_name=_('Paragraf'), null=True, blank=True)
    image = models.ImageField(
        verbose_name=_("Imagine"),
        help_text=_("Atașează o poză pentru paragraf"),
        upload_to="img/",
        default="images/default.png",
    )

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return str(self.title)
