from django.db import models

# Create your models here.
class PersonalRecord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField(null=True)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)

    def __unicode__(self):
        return self.first_name
