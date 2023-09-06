from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=40)


class Taluk(models.Model):
    district= models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

class Blood_bank(models.Model):
    dist= models.ForeignKey(District, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=40)
    class Meta:
        db_table = 'blood_bank'