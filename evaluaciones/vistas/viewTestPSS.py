from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts  import get_object_or_404
from evaluaciones.serializers import TestPSSSerializer, TestPSSSerializerGeneral
from evaluaciones.models import TestPSS
from usuarios.models import NewUser
from usuarios.mixins import ClienteKeyMixin
# Create your views here.

class CreateTestPSS(ClienteKeyMixin, CreateAPIView):
    serializer_class = TestPSSSerializer

class ListTestPSS(ClienteKeyMixin, ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestPSSSerializerGeneral
    queryset = TestPSS.objects.all()

class DetailTestPSS (ClienteKeyMixin, APIView):
    def post(self, request):
        email = request.user.email
        id_test = request.data["id_test"]
        user = get_object_or_404(NewUser, pk = email)
        queryset = TestPSS.objects.filter(pk = id_test, usuario=user)
        if queryset.exists():
            serializer = TestPSSSerializer(query_test)
            return Response(serializer.data)
        else:
            return Response({"Error": "No information"}, status=status.HTTP_404_NOT_FOUND)

class ListTestPSSPersonal(ClienteKeyMixin, APIView):
    def post(self, request):
        email = request.user.email
        user = get_object_or_404(NewUser, pk = email)
        queryset = TestPSS.objects.filter(usuario=user).order_by("created_at")
        serializer = TestPSSSerializerGeneral(queryset, many=True)
        return Response({"data": serializer.data, "user" : email}) 
