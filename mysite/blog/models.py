from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=90)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('post-detail', args=[self.slug])
    def pub_or_priv(self):
        """Returns 'public' or 'private' depending on whether visible is true or false"""
        if(self.visible == True):
            return 'Public'
        return 'Private'
    def get_username(self):
        """returns the author's username from the foreign key"""
        return self.author.username
    class Meta:
        #specify model field to order by
        ordering = ['date_added','title']

        #set default name of object
        def __unicode__(self):
            return u'%s' % self.title