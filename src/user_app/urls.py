from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user_app.views import registration_view, logout_view, user_profile_view

urlpatterns = [
    path("login/", obtain_auth_token),
    path("register/", registration_view),
    path("logout/", logout_view),

    #path("api/token/", TokenObtainPairView.as_view()),
    #path("api/token/refresh/", TokenRefreshView.as_view()).
    path("profile/", user_profile_view)
]