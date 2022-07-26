"""API rest"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin


class ApiViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):

    def list(self, request):
        lista = []
        lista.append({"text":"Hellou Mundo"})
        return Response(data=lista, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        dados = request.data
        body = {'id':pk, 'busca': True,'dados': dados}
        return Response(data=body, status=status.HTTP_200_OK)


    def create(self,request):
        body = request.data
        return Response(data=body, status=status.HTTP_201_CREATED)


    def delete(self, request, pk=None):
        if pk:
            body = request.data
            body = {'delete':True}
            status_code = status.HTTP_200_OK
        else:
            body = {'delete':False}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(data=body, status=status_code)


    def update(self, request, pk=None):
        body = request.data
        body.update({'atualizado':True})
        body.update({'id': pk})
        return Response(data=body, status=status.HTTP_200_OK)


    def partial_update(self, request, pk=None):
        body = request.data
        body.update({'parcial':True})
        body.update({'id': pk})
        return Response(data=body, status=status.HTTP_200_OK)
