from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Computer
from .serializers import ComputerSerializer


class ComputerListCreateView(APIView):
    def get(self, request):
        computers = Computer.objects.all()
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComputerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComputerDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Computer, pk=pk)

    def get(self, request, pk):
        computer = self.get_object(pk)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)

    def put(self, request, pk):
        computer = self.get_object(pk)
        serializer = ComputerSerializer(computer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        computer = self.get_object(pk)
        serializer = ComputerSerializer(computer, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        computer = self.get_object(pk)
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
