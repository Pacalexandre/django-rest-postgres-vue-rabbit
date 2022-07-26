from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin

class ApiViewSet(ListModelMixin, GenericViewSet):

    def list(self, request):
        return Response(data={"text":"Hellou Mundo"}, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        return Response(data={"text":pk}, status=status.HTTP_200_OK)

    def create(self,request):
        return Response(data={"text":"Hellou Mundo"}, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        return Response(data={}, status=status.HTTP_200_OK)
    
    def path(self, request, pk=None):
        return Response(data={}, status=status.HTTP_200_OK)


