from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from usuarios.view_tokens import MyTokenObtainPairView
from usuarios.views import CreateNewUser, ChangePassword, RecuperatePassword, UpdateInformation, DeleteUser, RestorePassword, TemplateRestorePassword, NumberofUsers

urlpatterns = [
    path("token/obtener/", MyTokenObtainPairView.as_view(), name="obtener-token"),
    path("token/refrescar/", TokenRefreshView.as_view(), name="refrescar-token"),
    path("token/verify/", TokenVerifyView.as_view(), name="verificar-token"),
    path("crearusuario/", CreateNewUser.as_view(), name="crear-usuario"),
    path("cambiar-contrasena/", ChangePassword.as_view(), name="cambiar-password"),
    path("recuperar-contraseña/", RecuperatePassword.as_view(), name="recuperar-contraseña"),
    path("actualizar-informacion/", UpdateInformation.as_view(), name="actualizar-informacion"),
    path("eliminar-usuario/", DeleteUser.as_view(), name="eliminar-usuario"),
    path("cambiar-password/", RestorePassword.as_view(), name="cambio-contraseña"),
    path("conteo-usuarios/", NumberofUsers.as_view(), name="Numero de usuarios"),
    re_path(r"cambiar/(?P<usr>)", TemplateRestorePassword.as_view(), name="template-recuperar-contraseña")
]
