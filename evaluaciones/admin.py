from django.contrib import admin
from evaluaciones.models import TestCSES26, TestSQV, TestSVS,TestPSS, TestCISCO, Consejos

# Register your models here.
admin.site.register(TestCSES26)
admin.site.register(TestSQV)
admin.site.register(TestSVS)
admin.site.register(TestPSS)
admin.site.register(TestCISCO)
admin.site.register(Consejos)