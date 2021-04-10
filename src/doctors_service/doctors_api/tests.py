"""
Test cases of Doctors Service
"""
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorSerializer
from .models import Doctor


# initialize the APIClient app
client = Client()


@api_view(['GET'])
def get_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        return Response({})


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