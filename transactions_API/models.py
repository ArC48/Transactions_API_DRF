from django.db import models


class Transaction(models.Model):
    user_id = models.IntegerField()
    transaction_id = models.CharField(max_length=100)
    transaction_time = models.DateTimeField()
    item_code = models.CharField(max_length=50)
    item_description = models.CharField(max_length=255)
    number_of_items_purchased = models.IntegerField()
    cost_per_item = models.FloatField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"Transaction {self.transaction_id} by User {self.user_id}"
