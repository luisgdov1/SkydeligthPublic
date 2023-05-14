from rest_framework import serializers
from usuarios.models import NewUser

class NewUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ["email","password","name", "sex", "edad",]
    
    def create(self, validated_data):
        return NewUser.objects.create_user(**validated_data)