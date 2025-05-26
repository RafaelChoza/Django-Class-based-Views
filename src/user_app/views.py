from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from user_app.serializers import RegistrationSerializer, UserProfileSerializer
from user_app import models

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    user = request.user
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

@api_view(["POST"])
def logout_view(request):

    if request.method == "POST":
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def registration_view(request):
    if request.method == "POST":
        seralizer = RegistrationSerializer(data=request.data)

        data = {}

        if seralizer.is_valid():
            account = seralizer.save()

            data["response"] = "Registro Exitoso"
            data["username"] = account.username
            data["email"] = account.email

            token = Token.objects.get(user=account).key
            data["token"] = token

            # refresh_token = RefreshToken.for_user(account)
            # data["token"] = {
            #     "refresh":str(refresh_token),
            #     "access":str(refresh_token.access_token)    
            # }
        else:
            return Response(seralizer.errors)
        
        return Response(data)