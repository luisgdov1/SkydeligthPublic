from rest_framework import serializers
from evaluaciones.models import TestSVS, TestCSES26, TestSQV, TestPSS, TestCISCO, Consejos

class TestSVSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSVS
        exclude = ("id_test", "total")
    
    def create(self, validated_data):
        cuestionario = TestSVS.objects.create(**validated_data)
        cuestionario.total_points()
        cuestionario.save()
        return cuestionario

class TestCSES26Serializer(serializers.ModelSerializer):
    class Meta:
        model = TestCSES26
        exclude = ("id_test", "total")
        
    def create(self, validated_data):
        cuestionario = TestCSES26.objects.create(**validated_data)
        cuestionario.total_points()
        cuestionario.save()
        return cuestionario
        
class TestSQVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSQV
        exclude = ("id_test", "total")
    
    def create(self, validated_data):
        cuestionario = TestSQV.objects.create(**validated_data)
        cuestionario.total_points()
        cuestionario.save()
        return cuestionario

class TestPSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPSS
        exclude = ("id_test", "total")
    
    def create(self, validated_data):
        cuestionario = TestPSS.objects.create(**validated_data)
        cuestionario.total_points()
        cuestionario.save()
        return cuestionario

class TestCISCOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCISCO
        exclude = ("id_test", "total")
    
    def create(self, validated_data):
        cuestionario = TestCISCO.objects.create(**validated_data)
        cuestionario.total_points()
        cuestionario.save()
        return cuestionario
    
class TestSVSSerializerGeneral(serializers.ModelSerializer):
    class Meta:
        model = TestSVS
        exclude = ("id_test",)

class TestCSES26SerializerGeneral(serializers.ModelSerializer):
    class Meta:
        model = TestCSES26
        exclude = ("id_test",)
        
class TestSQVSerializerGeneral(serializers.ModelSerializer):
    class Meta:
        model = TestSQV
        exclude = ("id_test",)
        
class TestPSSSerializerGeneral(serializers.ModelSerializer):
    class Meta:
        model = TestPSS
        exclude = ("id_test",)
    
class TestCISCOSerializerGeneral(serializers.ModelSerializer):
    class Meta:
        model = TestCISCO
        exclude = ("id_test",)

class ConsejosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consejos
        fields = '__all__'