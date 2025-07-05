from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Prediction
from .utils import predict_stock

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        from django.contrib.auth.models import User
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    result = None
    error_message = None
    if request.method == 'POST':
        ticker = request.POST['ticker']
        try:
            result = predict_stock(ticker)
            Prediction.objects.create(
                user=request.user,
                ticker=ticker,
                predicted_price=result["predicted_price"],
                metrics=result["metrics"],
                chart_1=result["chart_1"],
                chart_2=result["chart_2"]
            )
        except Exception as e:
            error_message = str(e)

    predictions = Prediction.objects.filter(user=request.user).order_by('-created')
    return render(request, 'dashboard.html', {
        'predictions': predictions,
        'result': result,
        'error_message': error_message
    })
