from django.db import models
from usuarios.models import NewUser

# Create your models here.

class BaseTest(models.Model):
    usuario = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(null=True, verbose_name="Total")
    pregunta1 = models.IntegerField(null=False, verbose_name="Pregunta 1")
    pregunta2 = models.IntegerField(null=False, verbose_name="Pregunta 2")
    pregunta3 = models.IntegerField(null=False, verbose_name="Pregunta 3")
    pregunta4 = models.IntegerField(null=False, verbose_name="Pregunta 4")
    pregunta5 = models.IntegerField(null=False, verbose_name="Pregunta 5")
    pregunta6 = models.IntegerField(null=False, verbose_name="Pregunta 6")
    pregunta7 = models.IntegerField(null=False, verbose_name="Pregunta 7")
    pregunta8 = models.IntegerField(null=False, verbose_name="Pregunta 8")
    pregunta9 = models.IntegerField(null=False, verbose_name="Pregunta 9")
    pregunta10 = models.IntegerField(null=False, verbose_name="Pregunta 10")
    pregunta11 = models.IntegerField(null=False, verbose_name="Pregunta 11")
    pregunta12 = models.IntegerField(null=False, verbose_name="Pregunta 12")
    pregunta13 = models.IntegerField(null=False, verbose_name="Pregunta 13")
    pregunta14 = models.IntegerField(null=False, verbose_name="Pregunta 14")
    pregunta15 = models.IntegerField(null=False, verbose_name="Pregunta 15")
    pregunta16 = models.IntegerField(null=False, verbose_name="Pregunta 16")
    pregunta17 = models.IntegerField(null=False, verbose_name="Pregunta 17")
    pregunta18 = models.IntegerField(null=False, verbose_name="Pregunta 18")
    pregunta19 = models.IntegerField(null=False, verbose_name="Pregunta 19")
    pregunta20 = models.IntegerField(null=False, verbose_name="Pregunta 20")
    class Meta:
        abstract = True
    
    def total_points(self):
        total_base = self.pregunta1 + self.pregunta2 + self.pregunta3 + self.pregunta4 + self.pregunta5 + self.pregunta6 + self.pregunta7+ self.pregunta8+ self.pregunta9+ self.pregunta10+ self.pregunta11+ self.pregunta12+ self.pregunta13+ self.pregunta14 + self.pregunta15 + self.pregunta16 + self.pregunta17 + self.pregunta18 + self.pregunta19 + self.pregunta20
        self.total = total_base
        
class TestSVS(BaseTest):
    id_test = models.AutoField(primary_key=True)
    total = models.FloatField(null=True, verbose_name="total")
    
    def __str__(self):
        return f'Test SVS no. {self.id_test}'
    
    def total_points(self):
        total_base = self.pregunta1 + self.pregunta2 + self.pregunta3 + self.pregunta4 + self.pregunta5 + self.pregunta6 + self.pregunta7+ self.pregunta8+ self.pregunta9+ self.pregunta10+ self.pregunta11+ self.pregunta12+ self.pregunta13+ self.pregunta14 + self.pregunta15 + self.pregunta16 + self.pregunta17 + self.pregunta18 + self.pregunta19 + self.pregunta20
        self.total = float(total_base)/20

class TestSQV(BaseTest):
    id_test = models.AutoField(primary_key=True)
    def __str__(self):
        return f'Test SQV no. {self.id_test}'

class TestCISCO(BaseTest):
    id_test = models.AutoField(primary_key=True)
    pregunta21 = models.IntegerField(null=False, verbose_name="Pregunta 21")

    def __str__(self):
        return f'Test CISCO no. {self.id_test}'
    
    def total_points(self):
        total_base = self.pregunta1 + self.pregunta2 + self.pregunta3 + self.pregunta4 + self.pregunta5 + self.pregunta6 + self.pregunta7+ self.pregunta8+ self.pregunta9+ self.pregunta10+ self.pregunta11+ self.pregunta12+ self.pregunta13+ self.pregunta14 + self.pregunta15 + self.pregunta16 + self.pregunta17 + self.pregunta18 + self.pregunta19 + self.pregunta20 + self.pregunta21
        self.total = total_base
    
class TestCSES26(BaseTest):
    id_test = models.AutoField(primary_key=True)
    pregunta21 = models.IntegerField(null=False, verbose_name="Pregunta 21")
    pregunta22 = models.IntegerField(null=False, verbose_name="Pregunta 22")
    pregunta23 = models.IntegerField(null=False, verbose_name="Pregunta 23")
    pregunta24 = models.IntegerField(null=False, verbose_name="Pregunta 24")
    pregunta25 = models.IntegerField(null=False, verbose_name="Pregunta 25")
    pregunta26 = models.IntegerField(null=False, verbose_name="Pregunta 26")
    
    def __str__(self):
        return f'Test CSES26 no. {self.id_test}'
    
    def total_points(self):
        total_base = self.pregunta1 + self.pregunta2 + self.pregunta3 + self.pregunta4 + self.pregunta5 + self.pregunta6 + self.pregunta7+ self.pregunta8+ self.pregunta9+ self.pregunta10+ self.pregunta11+ self.pregunta12+ self.pregunta13+ self.pregunta14 + self.pregunta15 + self.pregunta16 + self.pregunta17 + self.pregunta18 + self.pregunta19 + self.pregunta20 + self.pregunta21 + self.pregunta22 + self.pregunta23 + self.pregunta24 + self.pregunta25 + self.pregunta26
        self.total = total_base

class TestPSS(models.Model):
    id_test = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(null=True, verbose_name="Total")
    pregunta1 = models.IntegerField(null=False, verbose_name="Pregunta 1")
    pregunta2 = models.IntegerField(null=False, verbose_name="Pregunta 2")
    pregunta3 = models.IntegerField(null=False, verbose_name="Pregunta 3")
    pregunta4 = models.IntegerField(null=False, verbose_name="Pregunta 4")
    pregunta5 = models.IntegerField(null=False, verbose_name="Pregunta 5")
    pregunta6 = models.IntegerField(null=False, verbose_name="Pregunta 6")
    pregunta7 = models.IntegerField(null=False, verbose_name="Pregunta 7")
    pregunta8 = models.IntegerField(null=False, verbose_name="Pregunta 8")
    pregunta9 = models.IntegerField(null=False, verbose_name="Pregunta 9")
    pregunta10 = models.IntegerField(null=False, verbose_name="Pregunta 10")
    
    def __str__(self):
        return f'Test CSES26 no. {self.id_test}'
    def total_points(self):
        total_base = self.pregunta1 + self.pregunta2 + self.pregunta3 + self.pregunta4 + self.pregunta5 + self.pregunta6 + self.pregunta7+ self.pregunta8+ self.pregunta9+ self.pregunta10
        self.total = total_base
    
class Consejos(models.Model):
    id = models.AutoField(primary_key=True)
    consejo = models.TextField(blank=True, null=True)
    tipo_consejo = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'Consejo #{self.id}, tipo: {self.tipo_consejo}: {self.consejo}'
