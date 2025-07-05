from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, PredictView
from .views_frontend import register_view, login_view, logout_view, dashboard_view

urlpatterns = [
    path('register-api/', RegisterView.as_view(), name='register-api'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('predict/', PredictView.as_view(), name='predict'),

    # Frontend pages
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
