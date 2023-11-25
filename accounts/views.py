from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from applications.models import Applications

# Create your views here.
class AccountCreateView(CreateAPIView):
    serializer_class = CreateAccountSerializer
    permission_classes = [AllowAny]

    def perform_create(self,serializer):
        password1 = serializer.validated_data.pop('password1') 
        password2 = serializer.validated_data.pop('password2')

        if not password1 or not password2 or not (password1 == password2):
            print("bad passwords")
            raise ValidationError("Passwords do not match.") 
        
        Account.objects.create_user(**serializer.validated_data,  
                                              password=password1)
        
class AccountListView(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Account.objects.all().filter(isShelter = True)

class AccountRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # shelter needs to have an open application with the user to view the user
        # if shelter, then anyone can view
        if not instance.isShelter:
            if request.user.isShelter:
                open_apps = Applications.objects.filter(applicant = instance).filter(pet__shelter = request.user).first()
                if not open_apps:
                    return Response("You do not have any applications submitted by this account.",status=status.HTTP_403_FORBIDDEN)
            elif request.user.id != instance.id: # cannot get profile of another user
                return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    # PUT
    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        
        # owner check
        if request.user.id != pk:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)
    
    # PATCH- partial
    def partial_update(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        # owner check
        if request.user.id != pk:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        # owner check
        if request.user.id != pk:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        return super().destroy(request, *args, **kwargs)
    
    

    


    
    
