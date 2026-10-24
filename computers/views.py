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
