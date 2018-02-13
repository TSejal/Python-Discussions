from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Discussion(models.Model):
    
    discussion_type = (
			('article', 'Article'),
            ('question', 'Question'),
			('post', 'Post'), 
            ('blog', 'Blog'), 
		)

    title = models.CharField(max_length = 50)
    text = models.TextField()
    discussion_type = models.CharField(max_length = 10, choices = discussion_type)
    added_by = models.ForeignKey(User)
    is_published = models.BooleanField(default = True)
    created_date = models.DateTimeField(default = timezone.now)
    modified_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'discussions_img/')

    def __str__(self):
		return self.title


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion)
    text = models.TextField()
    added_by = models.ForeignKey(User)
    created_date = models.DateTimeField(default = timezone.now)
    modified_date = models.DateTimeField(default = timezone.now)

    # class Meta: 
    #     unique_together = ('discussion','added_by')

    def __str__(self):
		return self.text