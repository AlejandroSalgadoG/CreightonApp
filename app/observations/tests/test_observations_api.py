from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Observation
from observations.serializers import ObservationSerializer


OBSERVATIONS_URL = reverse("observation:observation-list")


def create_observation(user, **kwargs):
    attrs = {
        "date": date(year=2024, month=8, day=13),
        "observation": "6",
        "code": "C",
        "frequency": "x1",
    }
    attrs.update(kwargs)
    return Observation.objects.create(user=user, **attrs)


class PublicObservationAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(OBSERVATIONS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="test123",
        )
        self.client.force_authenticate(user=self.user)

    def test_retrive_observations(self):
        create_observation(user=self.user)
        create_observation(user=self.user)

        res = self.client.get(OBSERVATIONS_URL)

        observations = Observation.objects.all().order_by("-id")
        serializer = ObservationSerializer(observations, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_observation_list_limited_to_user(self):
        other_user = get_user_model().objects.create_user(
            email="other@example.com",
            password="test123",
        )

        create_observation(user=other_user)
        create_observation(user=self.user)

        res = self.client.get(OBSERVATIONS_URL)

        observations = Observation.objects.filter(user=self.user)
        serializer = ObservationSerializer(observations, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_observation(self):
        payload = {
            "date": date(year=2024, month=8, day=13),
            "observation": "6",
            "code": "C",
            "frequency": "x1",
        }
        res = self.client.post(OBSERVATIONS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        recipe = Observation.objects.get(id=res.data["id"])
        for k, v in payload.items():
            self.assertEqual(getattr(recipe, k), v)
        self.assertEqual(recipe.user, self.user)
