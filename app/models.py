
from django.db import models



EMP_CHOICES= [
    ('Employed', 'Employed'),
    ('Self-employed', 'Self-employed'),
    ('Out of work', 'Out of work'),
    ('Homemaker', 'Homemaker'),
    ]
# Create your models here.
class User(models.Model):
    emp=models.CharField(max_length=70,choices=EMP_CHOICES)
    title=models.CharField(max_length=70)
    email=models.EmailField(default='')
    description=models.TextField(max_length=90)
    # time=models.DateTimeField(auto_now_add=True)