from django.db import models


# Create your models here.

class User1(models.Model):
    userid = models.CharField(max_length=8, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    pword = models.CharField(max_length=20, blank=True, null=True)
    id = models.IntegerField(blank=True, null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbm_user'
