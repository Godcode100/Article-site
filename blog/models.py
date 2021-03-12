from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
#class Reporter(models.Model):
#    full_name = models.CharField(max=100)
    
#    def __str__(self):
#       return self.full_name
class Article(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(default =timezone.now)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()
    def __str__(self):
        return self.headline