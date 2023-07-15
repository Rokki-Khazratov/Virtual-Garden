from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
# from django.http import Http404

from apps.plants.models import Plants,UserProfile
from .serializers import PlantSerializer



class PlantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantSerializer

plant_list_create_view = PlantListCreateAPIView.as_view()

# class PlantDetailAPIView(generics.RetrieveAPIView):
#     queryset = Plants.objects.all()
#     serializer_class = PlantSerializer

#     def preform_create(self, serizlizer):
#         title = serizlizer.validated_data.get('title')
#         content = serizlizer.validated_data.get('content')
#         if content is None:
#             content = title
#         serizlizer.save(content = content)

# plant_detail_view = PlantDetailAPIView.as_view()



# @api_view(['GET', 'POST'])
# def plant_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method  

#     if method == "GET":
#         if pk is not None:
#             obj = get_object_or_404(Plant, pk=pk)
#             data = PlantSerializer(obj, many=False).data
#             return Response(data)
#         queryset = Plants.objects.all() 
#         data = PlantSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         serializer = PlantSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)