from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    predicted_price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    metrics = models.JSONField()
    chart_1 = models.CharField(max_length=200)
    chart_2 = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ticker} - {self.predicted_price}"
