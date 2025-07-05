
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # ✅ This includes /login/, /register/, etc.
    path('api/v1/', include('core.urls'))

]
