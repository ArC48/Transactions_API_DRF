from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "UserId",
            "TransactionId",
            "TransactionTime",
            "ItemCode",
            "ItemDescription",
            "NumberOfItemPurchased",
            "CostPerItem",
            "Country",
        ]
