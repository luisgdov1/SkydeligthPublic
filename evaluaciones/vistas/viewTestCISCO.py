from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts  import get_object_or_404
from evaluaciones.serializers import TestCISCOSerializer, TestCISCOSerializerGeneral
from evaluaciones.models import TestCISCO
from usuarios.models import NewUser
# Create your views here.
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from usuarios.mixins import ClienteKeyMixin

class CreateTestCISCO(ClienteKeyMixin, CreateAPIView):
    serializer_class = TestCISCOSerializer

class ListTestCISCO(ClienteKeyMixin, ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestCISCOSerializerGeneral
    queryset = TestCISCO.objects.all()

class DetailTestCISCO (ClienteKeyMixin, APIView):
    def post(self, request):
        email = request.user.email
        id_test = request.data["id_test"]
        user = get_object_or_404(NewUser, pk = email)  
        queryset = TestCISCO.objects.filter(pk = id_test, usuario=user)
        if queryset.exists():
            serializer = TestCISCOSerializer(query_test)
            return Response(serializer.data)
        else:
            return Response({"Error": "No information"}, status=status.HTTP_404_NOT_FOUND)
    
class ListTestCISCOPersonal(ClienteKeyMixin, APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.user.email
        user = get_object_or_404(NewUser, pk = email)
        queryset = TestCISCO.objects.filter(usuario=user).order_by("created_at")
        serializer = TestCISCOSerializerGeneral(queryset, many=True)
        return Response({"data": serializer.data, "user" : email}) 
