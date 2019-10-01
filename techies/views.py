from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from . models import talent
from rest_framework import filters
from . searializer import TalentSerializer
from django.db.models import Q
from rest_framework import permissions
from . permissions import IsConsultant

class Talents(viewsets.ViewSet):
    queryset = talent.objects.all()
    serializer_class = TalentSerializer
    permission_classes = [IsConsultant]
    def list(self, request):
        print(request)
        self.queryset = talent.objects.all()
        return Response(self.serializer_class(self.queryset, many=True).data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def create(self, request):
        if request.data is None:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def get_by_name(self,request):
        search_term = self.request.query_params.get('search')
        user = self.queryset.filter(Q(firstName__icontains=search_term)|Q(lastName__icontains=search_term))
        return Response(self.serializer_class(user,many=True).data, status=status.HTTP_200_OK)