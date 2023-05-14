from django.conf import settings
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


class ClienteKeyMixin:    
    def dispatch(self, request, *args, **kwargs):
        if "HTTP_KEY_CLIENT" not in request.META:
            raise PermissionDenied()
        if request.META["HTTP_KEY_CLIENT"] in settings.VALIDATIONS_CLIENTS_KEY:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied('Contact admin')