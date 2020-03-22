from rest_framework import serializers

from .models import Transaction, Segment


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ["project"]


class SegmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Segment
        exclude = ["transaction"]
