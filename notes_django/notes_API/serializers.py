from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.id')

    class Meta:
        model = Note
        fields = "__all__"
