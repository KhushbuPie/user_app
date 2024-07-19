# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Person
# from .serializers import PersonSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.decorators import action

# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

#     @action(detail=True, methods=['put'])
#     def custom_update(self, request, pk=None):
#         try:
#             person = Person.objects.get(pk=pk)
#         except Person.DoesNotExist:
#             return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=True, methods=['delete'])
#     def custom_delete(self, request, pk=None):
#         try:
#             person = Person.objects.get(pk=pk)
#         except Person.DoesNotExist:
#             return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # class UpdatePersonView(APIView):
# #     def put(self, request, pk):
# #         person = Person.objects.get(pk=pk)
# #         person.name = request.data.get('name')
# #         person.save()
# #         return Response({'message': 'Person updated successfully'})



from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer

class PersonListCreate(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetail(APIView):
    def get(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
