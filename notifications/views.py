from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from .models import Notifications
from .serializers import NotificationSerializer
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
        
class NotificationManageViewSet(ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
    
        if instance.owner != request.user:
            raise PermissionDenied('No permission')
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.owner != request.user:
            raise PermissionDenied('No permission')
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.owner != request.user:
            raise PermissionDenied('No permission')
        
        instance.read = True
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        try:
            sort = int(request.query_params.get('sort', 0))
            read = int(request.query_params.get('read', 0))
            page = int(request.query_params.get('page', 1))
        except ValueError:
            return Response({"Invalid Input, all parameters must be integers."}, status=status.HTTP_400_BAD_REQUEST)

        if sort not in [0, 1]:
            return Response({"Invalid value for 'sort'."}, status=status.HTTP_400_BAD_REQUEST)

        if read not in [0, 1]:
            return Response({"Invalid value for 'read'."}, status=status.HTTP_400_BAD_REQUEST)

        if page < 1:
            return Response({"Invalid value for 'page'."}, status=status.HTTP_400_BAD_REQUEST)
        current_user = request.user
        page_size = 10
        start = (page - 1) * page_size
        end = page * page_size


        if read == None or read == 0:
            is_read = False
        else:
            is_read = True
        
        list_ordered = Notifications.objects
        if sort:
            list_ordered = list_ordered.order_by('-creation_time')
        else:
            list_ordered = list_ordered.order_by('creation_time')
            
        list_info = list_ordered.filter(read=is_read).filter(owner=current_user)[start:end]
        serializer = self.get_serializer(list_info, many=True)

        return Response(serializer.data)
        

    def get_queryset(self):
        return Notifications.objects.all() 