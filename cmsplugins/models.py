from django.db import models
from colorfield.fields import ColorField
from cms.models.pluginmodel import CMSPlugin
from djangocms_text.fields import HTMLField
from filer.fields.image import FilerImageField
# Create your models here.


class ContentContainer(CMSPlugin):
    background_color = ColorField(default = "#FFFFFF")
    

    def __str__(self):
        return f'Die Hintergrundfarbe ist {self.background_color}'

class FirstContentItem(CMSPlugin):
    title = models.CharField(max_length=50, blank=True)
    text =  HTMLField(blank=True)
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name="images")
    background_color = ColorField(default='#000000')

    def __str__(self):
        return self.title