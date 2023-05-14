from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from usuarios.serializers import NewUserSerializers
from usuarios.models import NewUser
from usuarios.mixins import ClienteKeyMixin
from usuarios.utils.send_email import send_email_reset
# Create your views here.
from django.views.generic import TemplateView, View

class CreateNewUser(ClienteKeyMixin, CreateAPIView):
    serializer_class = NewUserSerializers
    permission_classes = [AllowAny,]

class ChangePassword(ClienteKeyMixin, APIView):
    def put(self, request):
        #Cambiar la contraseña
        email = request.user.email
        password = request.data["password"]
        user = get_object_or_404(NewUser, pk=email)
        user.set_password(password)
        user.save()
        return Response({"Message" : "Success the password is changed"})

class RecuperatePassword(APIView):
    permission_classes = [AllowAny,]
    
    def post(self, request):
        email = request.data["email"]
        user = get_object_or_404(NewUser, pk=email)
        token = RefreshToken.for_user(user)
        user.required_password = True
        user.save()
        print(token)
        url_personal = f'https://apiskydelight.herokuapp.com/usuarios/cambiar/?usr={token.access_token}'
        send_email_value = send_email_reset(user.email, user.name, url_personal)
        if send_email_value:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

class UpdateInformation(ClienteKeyMixin, APIView):
    def put(self, request):
        user = get_object_or_404(NewUser, pk=request.user.email)
        if request.data["name"] != "" or request.data["name"] != None:
            user.name = request.data["name"]
        if request.data["sex"] != "" or request.data["sex"] != None:
            user.sex = request.data["sex"]
        if request.data["edad"] != "" or request.data["edad"] != None and request.data["edad"].isnumeric():
            user.edad = request.data["edad"]
        user.save()
        return Response({"Success" : "Informacion actualizada"}, status=status.HTTP_200_OK)

class DeleteUser(ClienteKeyMixin, APIView):
    def put(self, request):
        user = get_object_or_404(NewUser, pk=request.user.email)
        email = user.email
        user.delete()
        return Response({"Success": f'Usuario {email} eliminado'}, status=status.HTTP_202_ACCEPTED)

class RestorePassword(APIView):
    def post(self, request):
        print("Si entra")
        email =  request.user.email
        user = get_object_or_404(NewUser, pk=email)
        if user.required_password == True:
            password = request.data["password"]
            user.set_password(password)
            user.required_password = False
            user.save()
            RefreshToken.for_user(user)
            return Response({"Succes": "Password changed"}, status=status.HTTP_200_OK)
        return Response({"Error": "No validate"}, status=status.HTTP_409_CONFLICT)
        
class TemplateRestorePassword(TemplateView):
    template_name = "password_changes.html"
    permission_classes = [AllowAny,]
    
    
class NumberofUsers(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        count_users = NewUser.objects.all().count()
        return Response({"Conteo": count_users}, status=status.HTTP_200_OK)
        
