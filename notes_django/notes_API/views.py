from .serializers import NoteSerializer
from .models import Note
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status


class NoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # return list of notes, created by current user
        queryset = Note.objects.filter(creator=request.user, archived=False)
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # return note by it's id
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, pk=pk)
        if note.creator != request.user:
            return Response({
                "Error": "You dont have access to this note"
            }, status=status.HTTP_403_FORBIDDEN)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        # update note fields
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, pk=pk)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if request.user != note.creator:
            return Response({
                "Error": "You dont have access to this note"
            }, status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        # create note field
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        # change archived flag to true
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, pk=pk)
        if request.user != note.creator:
            return Response({
                "Error": "You dont have access to this note"
            }, status=status.HTTP_403_FORBIDDEN)
        note.archived = True
        note.save()
        return Response({"Note successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
