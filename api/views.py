from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework import permissions

from api.serializers import userSerializer, loginSerializer, StudentDetails, booksSerializer, updateSerializer

from . models import userModel, booksModel
from wkhtmltopdf.views import PDFTemplateView
from datetime import date, datetime
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class registerUser(GenericAPIView):
    serializer_class = userSerializer
    permission_classes = (permissions.AllowAny,)
    @method_decorator(cache_page(CACHE_TTL))
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"user registered succeesfuly"},status=status.HTTP_201_CREATED)

        return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
class loginUser(GenericAPIView):
    serializer_class = loginSerializer
    @method_decorator(cache_page(CACHE_TTL))
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = authenticate(request, username=request.data['username'], password=request.data['password'])
            if user is not None:
                login(request, user)
                request.session['logged_in'] = True
                request.session['username'] = request.data['username']
                return Response({"message":"you are logged in"}, status=status.HTTP_201_CREATED)
            else:
                error_message = "Invalid username or password."
                return Response({'error_message': error_message})
        else:
            error_message = "Invalid username or password."
            return Response({'error_message': error_message})
        
class MyProtectedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = userModel.objects.all()

    def get(self, request):
        content = {'message': 'You are authenticated and authorized to access this view!'}
        return Response(content)        
    
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({"message": "You have been logged out."})    

class ListUsers(ListAPIView):
    serializer_class = StudentDetails
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return userModel.objects.filter(username=self.request.user)    
    
class addBooks(CreateAPIView):
    serializer_class = booksSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class booksListView(ListAPIView):
    serializer_class = booksSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return booksModel.objects.filter(user=self.request.user) 

class booksUpdate(UpdateAPIView):
    serializer_class = updateSerializer   
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return booksModel.objects.filter(user=self.request.user)

class deleteBook(DestroyAPIView):
    queryset = booksModel.objects.all()
    serializer_class = booksSerializer

class pdfReport(PDFTemplateView):
    template_name = 'user_pdf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['date'] = datetime.now()
        return context

    def get_filename(self):
        filename = self.request.user.username + str(datetime.now())
        return f'{filename}.pdf'


class hello(GenericAPIView):
    def get(self, request):
        return Response({"hello"})