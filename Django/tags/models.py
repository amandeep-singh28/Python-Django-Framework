from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length = 255)

class  TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    # Now we need to identify on which object this tag is applied to
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE) # Type of the object
    object_id = models.PositiveIntegerField() # ID
    content_object = GenericForeignKey() # Actual Python Object
