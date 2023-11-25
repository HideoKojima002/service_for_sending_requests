from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Request
from .serializers import RequestSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import requests
import time
import random


def send_request(cadastre_number, latitude, longitude): # Эмуляция отправки запроса на внешний сервер
    delay = random.randint(0, 60)
    time.sleep(delay)
    result = random.choice([True, False])
    return result


# @api_view(['POST'])
class RequestCreateViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Получаем данные из запроса и проверяем их валидность
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        result = send_request(**data)  # Вызываем функцию для эмуляции отправки запроса на внешний сервер
        request = Request.objects.create(**data, result=result)
        headers = self.get_success_headers(serializer.data)
        return Response(RequestSerializer(request).data, status=status.HTTP_201_CREATED, headers=headers)


# @api_view(['GET'])
class PingViewSet(viewsets.ViewSet):
    def list(self, request):
        return JsonResponse({'message': 'Server is running'}, status=status.HTTP_200_OK)


# @api_view(['GET'])
class HistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# @api_view(['GET'])
# @csrf_exempt
# def ping(request):
#     return JsonResponse({'message': 'Server is running'}, status=status.HTTP_200_OK)


class ResultRetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        result = instance.result
        return Response({'result': result}, status=status.HTTP_200_OK)




# @api_view(['GET'])
# class ResultViewSet(viewsets.ViewSet):
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# class ResultViewSet(viewsets.ViewSet):
#     def retrieve(self, request, pk=None):
#         try:
#             request = Request.objects.get(id=pk)
#         except Request.DoesNotExist:
#             return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = RequestSerializer(request)
#         return Response(serializer.data, status=status.HTTP_200_OK)
