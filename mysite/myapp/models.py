from django.db import models

# Create your models here.
class Quest(models.Model):
    user_name = models.CharField(max_length=30)
    title_field = models.CharField(max_length=30)
    date_field = models.DateField(auto_now=True)
    task_field = models.CharField(max_length=256)
    reward_field = models.CharField(max_length=100)

    def __str__(self):
        return self.title_field
