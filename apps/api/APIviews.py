from rest_framework import generics, status
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = serializer.data

        include_plants = request.query_params.get('plants') == 'true'
        if include_plants:
            plants = instance.plants.all()
            plant_serializer = PlantSerializer(plants, many=True, context={'request': request})
            response_data = plant_serializer.data

        return Response(response_data)
    
profile_list_view = ProfileListAPIView.as_view()



@api_view(['POST'])
def add_to_cart(request, id):
    try:
        user_profile = UserProfile.objects.get(user_id=id)
        print('first try test ')
    except UserProfile.DoesNotExist:
        return Response({'error': 'UserProfile not found.'}, status=status.HTTP_404_NOT_FOUND)

    plant_id = request.data.get('plant_id')
    print(plant_id)
    try:
        plant = Plants.objects.get(pk=plant_id)
        print("second try test")
    except Plants.DoesNotExist:
        return Response({'error': 'Plant not found.'}, status=status.HTTP_404_NOT_FOUND)

    user_profile.cart.add(plant)
    return Response({'message': 'Plant added to cart successfully.'}, status=status.HTTP_200_OK)



class UserProfileCartDeleteView(generics.DestroyAPIView):
    serializer_class = PlantSerializer

    def destroy(self, request, *args, **kwargs):
        user_id = kwargs['id']
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return Response({'error': 'UserProfile not found.'}, status=status.HTTP_404_NOT_FOUND)

        plant_id = kwargs['plant_id']
        try:
            plant = Plants.objects.get(pk=plant_id)
        except Plants.DoesNotExist:
            return Response({'error': 'Plant not found.'}, status=status.HTTP_404_NOT_FOUND)

        user_profile.cart.remove(plant)
        return Response({'message': 'Plant removed from cart successfully.'}, status=status.HTTP_200_OK)



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