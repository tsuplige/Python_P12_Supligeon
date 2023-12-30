# from django.shortcuts import render
from rest_framework import generics
from .models import Client, Contract, Event
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import ClientDetailSerializer, ClientListSerializer, ContractSerializer, EventSerializer


class ClientViewset(ReadOnlyModelViewSet):

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_queryset(self):
        return Client.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return self.detail_serializer_class


class ContractViewset(ReadOnlyModelViewSet):

    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()


class EventViewset(ReadOnlyModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
