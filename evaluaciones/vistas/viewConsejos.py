import random
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts  import get_object_or_404
from evaluaciones.models import Consejos
from evaluaciones.serializers import ConsejosSerializer
from usuarios.mixins import ClienteKeyMixin

class GetConsejo (APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        id_excluded = eval(request.data["list_excluded"])
        tipo_consejo = request.data["type_advice"]
        if tipo_consejo == "especifico":
            consejos = Consejos.objects.filter(tipo_consejo="especifico").exclude(id__in=id_excluded)
            object_consejo =  consejos.order_by("?").first()
            serializer_data = ConsejosSerializer(object_consejo)
            return Response(serializer_data.data)
        else:
            consejos = Consejos.objects.exclude(tipo_consejo="especifico")
            object_consejo = consejos.order_by("?").first()
            serializer_data = ConsejosSerializer(object_consejo)
            return Response(serializer_data.data)
