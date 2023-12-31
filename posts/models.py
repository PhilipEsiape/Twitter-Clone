from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField('Name', blank=False,null=False, max_length=14, db_index=True, default='Anonymous')

    body = models.CharField('Body', blank=True, null=True, max_length=140,db_index=True)

    created_at = models.DateTimeField('created_dateTime',blank=True , auto_now_add=True)

    image = CloudinaryField('Image', blank=True)

    likes = models.PositiveIntegerField('like', default=0, blank=True, db_index=True)
   