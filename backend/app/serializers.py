from rest_framework import serializers
from .models import Cliente, Fornitore

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'partita_iva', 'email']

class FornitoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornitore
        fields = ['id', 'nome', 'partita_iva', 'email']