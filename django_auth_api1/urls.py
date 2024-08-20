from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
    path('', views.get_routes),
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
]
