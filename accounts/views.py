from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .serializers import *


class RegisterAPIView(APIView):

    @swagger_auto_schema(
        request_body=AccountSerializer
    )
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                username=serializer.validated_data.get('phone_number'),
            )
            response = {
                'success': True,
                'message': 'Account created successfully.',
                'data': serializer.data
            }
            return Response(response, status=HTTP_201_CREATED)
        response = {
            'success': False,
            'message': 'Account creation failed.',
            'error': serializer.errors
        }
        return Response(response, status=HTTP_400_BAD_REQUEST)


class AccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer

    def get_object(self):
        return self.request.user
