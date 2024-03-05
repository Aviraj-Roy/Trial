from django.db import models

# Create your models here.
class Userdetails(models.Model):
        id=models.AutoField(primary_key=True)
        username = models.CharField(max_length=200)
        password  = models.CharField(max_length = 200)
        email = models.EmailField(max_length=200)
        date = models.DateTimeField(max_length=200)

        class Meta:
            db_table="userinfo"