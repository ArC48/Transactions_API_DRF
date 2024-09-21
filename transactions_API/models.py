from django.db import models


class Transaction(models.Model):
    UserId = models.IntegerField()
    TransactionId = models.CharField(max_length=100)
    TransactionTime = models.DateTimeField()
    ItemCode = models.CharField(max_length=50)
    ItemDescription = models.CharField(max_length=255)
    NumberOfItemsPurchased = models.IntegerField()
    CostPerItem = models.FloatField()
    Country = models.CharField(max_length=50)

    def __str__(self):
        return f"Transaction {self.transaction_id} by User {self.user_id}"


class Purchase(models.Model):
    TransactionTime = models.DateTimeField()
    NumberOfItemsPurchased = models.IntegerField()
