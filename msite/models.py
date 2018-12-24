from django.db import models

class Url(models.Model):
    noUrl = models.IntegerField(primary_key=True)
    noParent = models.IntegerField()
    value = models.CharField(max_length=2083, default=None,null=True)
    depth = models.IntegerField()

    def __unicode__(self):
        return self.value