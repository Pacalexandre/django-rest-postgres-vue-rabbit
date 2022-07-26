
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin


class ApiViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    def list(self, request):
        return Response(data={"text":"Hellou Mundo"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        body = {'id':pk, 'busca': True}
        return Response(data=body, status=status.HTTP_200_OK)

    def create(self,request):
        body = request.data
        return Response(data=body, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None):
        if pk:
            body = request.data
            body = {'delete':True}
            status = status.HTTP_200_OK
        else:
            body = {'delete':False}
            status = status.HTTP_400
        return Response(data=body, status=status)

    def update(self, request, pk=None):
        body = request.data
        body.update({'atualizado':True})
        body.update({'id': pk})
        return Response(data=body, status=status.HTTP_200_OK)
