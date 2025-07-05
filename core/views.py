from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .utils import predict_stock
from .models import Prediction

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ticker = request.data.get("ticker")
        if not ticker:
            return Response({"error": "Ticker is required."}, status=400)

        result = predict_stock(ticker)

        Prediction.objects.create(
            user=request.user,
            ticker=ticker,
            predicted_price=result["predicted_price"],
            metrics=result["metrics"],
            chart_1=result["chart_1"],
            chart_2=result["chart_2"]
        )

        return Response({
            "ticker": ticker,
            "next_day_price": result["predicted_price"],
            "mse": result["metrics"]["mse"],
            "rmse": result["metrics"]["rmse"],
            "r2": result["metrics"]["r2"],
            "plot_urls": [result["chart_1"], result["chart_2"]]
        })
