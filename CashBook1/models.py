from django.db import models


# Create your models here.
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=100)
    cur = models.IntegerField(null=False)


    class Meta:
        db_table = "Account"


class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    data_date = models.DateField(null=False)
    narration = models.CharField(max_length=100)
    cd = models.IntegerField(null=False)
    amount = models.FloatField(null=False)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = "Data"