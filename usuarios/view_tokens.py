from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer,self).validate(attrs)
        data.update({'user': self.user.email})
        data.update({'name': self.user.name})
        data.update({'sex': self.user.sex})
        data.update({'age': self.user.edad})
        return data
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer