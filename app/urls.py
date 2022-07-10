from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

pair_view = TokenObtainPairView.as_view()
refresh_view = TokenRefreshView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/token", pair_view, name="token_obtain_pair"),
    path("api/token/refresh", refresh_view, name="token_refresh"),
    path('api/', include('employees.urls')),
]
