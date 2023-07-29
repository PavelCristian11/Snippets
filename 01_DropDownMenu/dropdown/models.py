from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Books(models.Model):
    first_name = models.CharField(max_length=255, null=False, name="First name")
    last_name = models.CharField(max_length=255, null=False, name='Last name')
    book_name = models.CharField(max_length=255, null=False)
    publish_year = models.PositiveIntegerField(default=1800, validators=[MinValueValidator(100), MaxValueValidator(2023)], name='year')
    price = models.DecimalField(max_digits=10, decimal_places=2, name = 'price')

    # def __str__(self):
    #     return self.first_name+'_'+self.last_name+'_'+self.book_name