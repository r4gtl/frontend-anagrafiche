from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cliente, Fornitore
from .serializers import ClienteSerializer, FornitoreSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class FornitoreViewSet(viewsets.ModelViewSet):
    queryset = Fornitore.objects.all()
    serializer_class = FornitoreSerializer
    permission_classes = [permissions.IsAuthenticated]

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            'totale_clienti': Cliente.objects.count(),
            'totale_fornitori': Fornitore.objects.count(),
        })