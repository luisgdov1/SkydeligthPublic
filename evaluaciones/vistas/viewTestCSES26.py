from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts  import get_object_or_404
from evaluaciones.serializers import TestCSES26Serializer, TestCSES26SerializerGeneral
from evaluaciones.models import TestCSES26
from usuarios.models import NewUser
# Create your views here.
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from usuarios.mixins import ClienteKeyMixin

class CreateTestCSES26(ClienteKeyMixin, CreateAPIView):
    serializer_class = TestCSES26Serializer

class ListTestCSES26(ClienteKeyMixin, ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestCSES26SerializerGeneral
    queryset = TestCSES26.objects.all()

class DetailTestCSES26 (ClienteKeyMixin, APIView):
    def post(self, request):
        email = request.user.email
        id_test = request.data["id_test"]
        user = get_object_or_404(NewUser, pk = email)  
        queryset = TestCSES26.objects.filter(pk = id_test, usuario=user).order_by("created_at")
        if queryset.exists():
            serializer = TestCSES26Serializer(query_test)
            return Response(serializer.data)
        else:
            return Response({"Error": "No information"}, status=status.HTTP_404_NOT_FOUND)
    
class ListTestCSES26Personal(ClienteKeyMixin, APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.user.email
        user = get_object_or_404(NewUser, pk = email)
        queryset = TestCSES26.objects.filter(usuario=user)
        serializer = TestCSES26SerializerGeneral(queryset, many=True)
        return Response({"data": serializer.data, "user" : email}) 
