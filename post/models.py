from django.db import models

# Create your models here.
class Volunteer(models.Model):

    GENDER_CHOICE=(
        ('남자','남자'),
        ('여자','여자'),
    )

    name=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=6,choices=GENDER_CHOICE)
    text=models.TextField()
    date=models.DateTimeField()
    image = models.ImageField(upload_to="post_img",blank=True, null=True)