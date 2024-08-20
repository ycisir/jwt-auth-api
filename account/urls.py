from django.urls import path
from account import views
urlpatterns = [
    path('signup/', views.UserSignup.as_view(), name='signup'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('passward-change/', views.UserChangePassword.as_view(), name='passward-change'),
    path('send-reset-passward-email/', views.SendPasswordResetEmail.as_view(), name='send-reset-passward-email'),
    path('reset-password/<uid>/<token>/', views.UserPasswordReset.as_view(), name='reset-password'),
]