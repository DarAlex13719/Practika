from django.db import models

class Nomera(models.Model):
    user_name = models.CharField(max_length=40, blank=False)
    email = models.EmailField()
    comment = models.TextField(max_length=500)
    #is_approved = models.BooleanField(default=False, verbose_name='Проверено')

def __str__(self):
    return f'{self.user_name} : {self.comment}'

# Create your models here.
