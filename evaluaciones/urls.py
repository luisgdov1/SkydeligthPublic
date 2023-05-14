from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from evaluaciones.vistas.viewTestCSES26 import DetailTestCSES26, ListTestCSES26, CreateTestCSES26, ListTestCSES26Personal
from evaluaciones.vistas.viewTestSQV import DetailTestSQV, ListTestSQV, CreateTestSQV, ListTestSQSPersonal
from evaluaciones.vistas.viewTestSVS import DetailTestSVS, ListTestSVS, CreateTestSVS, ListTestSVSPersonal
from evaluaciones.vistas.viewTestPSS import DetailTestPSS, ListTestPSS, CreateTestPSS, ListTestPSSPersonal
from evaluaciones.vistas.viewTestCISCO import DetailTestCISCO, ListTestCISCO, CreateTestCISCO, ListTestCISCOPersonal
from evaluaciones.vistas.viewConsejos import GetConsejo

urlpatterns = [
    path('consejo', GetConsejo.as_view(), name="tomar-consejo"),
    
    path('crear-testcses26', CreateTestCSES26.as_view(), name="crear-test-cses26"),
    path('lista-testcses26', ListTestCSES26.as_view(), name="lista-test-cses26"),
    path('detalle-testcses26', DetailTestCSES26.as_view(),name="detalle-test-cses26"),
    path('lista-testcses26-personal/', ListTestCSES26Personal.as_view(), name="lista-test-cses26-personal"),
    
    path('crear-testsqv', CreateTestSQV.as_view(), name="crear-test-sqv"),
    path('lista-testsqv', ListTestSQV.as_view(), name="lista-test-sqv"),
    path('detalle-testsqv', DetailTestSQV.as_view(), name="detalle-test-sqv"),
    path('lista-testsqv-personal/', ListTestSQSPersonal.as_view(), name="lista-test-sqv-personal"),
    
    path('crear-testsvs', CreateTestSVS.as_view(), name="crear-test-svs"),
    path('lista-testsvs', ListTestSVS.as_view(), name="lista-test-svs"),
    path('detalle-testsvs', DetailTestSVS.as_view(), name="detalle-test-svs"),
    path('lista-testsvs-personal/', ListTestSVSPersonal.as_view(), name="lista-test-svs-personal"),
    
    path('crear-testpss', CreateTestPSS.as_view(), name="crear-test-pss"),
    path('lista-testpss', ListTestPSS.as_view(), name="lista-test-pss"),
    path('detalle-testpss', DetailTestPSS.as_view(), name="detalle-test-pss"),
    path('lista-testpss-personal/', ListTestPSSPersonal.as_view(), name="lista-test-pss-personal"),
    
    path('crear-testcisco', CreateTestCISCO.as_view(), name="crear-test-cisco"),
    path('lista-testcisco', ListTestCISCO.as_view(), name="lista-test-cisco"),
    path('detalle-testcisco', DetailTestCISCO.as_view(), name="detalle-test-cisco"),
    path('lista-testcisco-personal/', ListTestCISCOPersonal.as_view(), name="lista-test-cisco-personal"),
]

