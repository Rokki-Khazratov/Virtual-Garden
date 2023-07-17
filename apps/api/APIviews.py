from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
# from django.http import Http404

from apps.plants.models import Plants,UserProfile
from .serializers import PlantSerializer,ProfileSerializer


class ProfileListAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

profile_list_views = ProfileListAPIView.as_view()


    


class PlantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantSerializer

plant_list_create_view = PlantListCreateAPIView.as_view()

class PlantDetailAPIView(generics.RetrieveAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        info = serializer.validated_data.get('info')
        if info is None:
            info = name
        serializer.save(info=info)

plant_detail_view = PlantDetailAPIView.as_view()

class PlantUpdateAPIView(generics.UpdateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'pk'  # Set the lookup field to 'pk'

plant_update_view = PlantUpdateAPIView.as_view()

class PlantDestroyAPIView(generics.DestroyAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'pk'  # Set the lookup field to 'pk'

plant_delete_view = PlantDestroyAPIView.as_view()



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
#             name = serializer.validated_data.get('name')
#             info = serializer.validated_data.get('info') or None
#             if info is None:
#                 info = name
#             serializer.save(info=info)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)