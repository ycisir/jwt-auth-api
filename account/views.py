from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import (
    UserSignupSerializer, UserLoginSerializer, UserProfileSerializer, 
    UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken

# generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserSignup(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token,'message':'User created successfully'}, status = status.HTTP_201_CREATED)
    

class UserLogin(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token,'message':'Logged in successfully'}, status = status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password in not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        

class UserProfile(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePassword(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        context = {
            'user': request.user,
        }
        serializer = UserChangePasswordSerializer(data=request.data, context=context)

        serializer.is_valid(raise_exception=True)
        return Response({'message':'Password changed successfully'}, status = status.HTTP_200_OK)
    
class SendPasswordResetEmail(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message':'Password reset link send. Please check your email'}, status = status.HTTP_200_OK)
        
class UserPasswordReset(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        context = {
            'uid':uid,
            'token':token
        }
        serializer = UserPasswordResetSerializer(data=request.data, context=context)

        serializer.is_valid(raise_exception=True)
        return Response({'message':'Password reset successfully'}, status = status.HTTP_200_OK)