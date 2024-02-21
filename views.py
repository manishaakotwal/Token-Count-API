
# Add these lines at the beginning of your views.py or a main script.
import django
from django.conf import settings
django.setup()
import os
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import tiktoken
from .serializers import* # Fixed import TokenCountSerializer 

class TokenCountAPIView(APIView):
    def post(self, request):
        print("Request data:", request.data)  # Debugging statement
        serializer =TokenCountSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            token_count = self.count_token(text, 'cl100k_base')  # Call count_token method
            return Response({'token_count': token_count, "text_return":text}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def count_token(self, text: str, enc_str: str) -> int:# Added self as it's a method of the class
        try:
            encoded = tiktoken.get_encoding(enc_str)
            token_count = len(encoded.encode(text))
            return token_count
        except Exception as e:
            print("Error in count_token:", e)  # Debugging statement
            return 0  # Handle error gracefully
        