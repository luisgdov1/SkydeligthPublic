from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts  import get_object_or_404
from evaluaciones.serializers import TestSVSSerializer, TestSVSSerializerGeneral
from evaluaciones.models import TestSVS
from usuarios.models import NewUser
from usuarios.mixins import ClienteKeyMixin

# Create your views here.

class CreateTestSVS(ClienteKeyMixin, CreateAPIView):
    serializer_class = TestSVSSerializer

class ListTestSVS(ClienteKeyMixin, ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestSVSSerializerGeneral
    queryset = TestSVS.objects.all()

class DetailTestSVS (ClienteKeyMixin, APIView):
    def post(self, request):
        email = request.user.email
        id_test = request.data["id_test"]
        user = get_object_or_404(NewUser, pk = email)
        queryset = TestSVS.objects.filter(pk = id_test, usuario=user)
        if queryset.exists():
            serializer = TestSVSSerializer(query_test)
            return Response(serializer.data)
        else:
            return Response({"Error": "No information"}, status=status.HTTP_404_NOT_FOUND)

class ListTestSVSPersonal(ClienteKeyMixin, APIView):
    def post(self, request):
        email = request.user.email
        user = get_object_or_404(NewUser, pk = email)
        queryset = TestSVS.objects.filter(usuario=user).order_by("created_at")
        serializer = TestSVSSerializerGeneral(queryset, many=True)
        return Response({"data": serializer.data, "user" : email}) 
