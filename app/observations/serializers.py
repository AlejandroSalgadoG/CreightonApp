from rest_framework import serializers

from core.models import Observation


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ["id", "date", "observation", "code", "frequency"]
        read_only_fields = ["id"]