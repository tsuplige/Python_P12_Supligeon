from rest_framework import serializers
from .models import Client, Contract, Event


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'compagny_name', 'support_contact']


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
