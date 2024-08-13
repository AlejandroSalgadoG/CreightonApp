from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Observation
from observations import serializers


class ObservationsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObservationSerializer
    queryset = Observation.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # overwrite default method to filter recipes of auth user
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def perform_create(self, serializer):
        # save recipie with authenticated user
        serializer.save(user=self.request.user)