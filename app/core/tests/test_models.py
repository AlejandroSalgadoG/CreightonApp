from datetime import date

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    def test_create_user_With_email_successful(self):
        email = "test@example.com"
        password = "test123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,  # password is hashed
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))  # compare hashed password

    def test_new_user_email_normalized(self):
        sample_emails =[
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@EXAMPLE.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_wo_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_observation(self):
        user = get_user_model().objects.create_user(
            email="test@example.com",
            password="test123",
        )

        observation = models.Observation.objects.create(
            user=user,
            date=date(year=2024, month=8, day=13),
            observation="6",
            code="C",
            frequency="x1",
        )

        observations = models.Observation.objects.all()
        
        self.assertEqual(observations.count(), 1)

        observation = observations[0]
        self.assertEqual(observation.user, user)
        self.assertEqual(observation.date, date(year=2024, month=8, day=13))
        self.assertEqual(observation.observation, "6")
        self.assertEqual(observation.code, "C")
        self.assertEqual(observation.frequency, "x1")
