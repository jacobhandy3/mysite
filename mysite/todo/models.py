from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timezone

# Create your models here.
class Task(models.Model):
    #priority of to do items choices 1-5
    priorities = [(1,'high'),(2,'medium-high'),(3,'medium'),(4,'medium-low'),(5,'low')]

    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.TextField()
    date_added = models.DateField(auto_now_add=True,editable=False)
    date_due = models.DateTimeField(null=True)
    priority = models.IntegerField(choices=priorities,default=5)

    def listPriorities(self):
        return Task.priorities
    def describePriority(self):
        return self.priorities[self.priority-1][1]
    def timeRemaining(self):
        remain = self.date_due.date() - datetime.now(timezone.utc).date()
        days = remain.days
        tdtos = "%s days"%days
        return tdtos
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('task-detail', args=[str(self.id)])
    
    class Meta:
        #specify model field to order by
        ordering = ['priority','date_due']

        #set default name of object
        def __unicode__(self):
            return u'%s' % self.title