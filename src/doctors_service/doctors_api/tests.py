"""
Test cases of Doctors Service
"""
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .serializers import DoctorSerializer
from .models import Doctor


# initialize the APIClient app
client = Client()


class GetAllDoctorsTest(TestCase):
    """ Test module for GET all doctors API """

    fixtures = ["doctors.yaml"]

    def test_get_all_doctors(self):
        # get API response
        response = client.get(reverse('doctor-list'))
        # get data from db
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
