"""
Serialisers for Doctors Service
"""
from rest_framework import serializers
from .models import Doctor, DoctorCharges, DoctorOpeningHours, DoctorAddressLanguage


class DoctorChargesSerializer(serializers.ModelSerializer):
    """
    Serislises Doctor Charges
    """

    class Meta:
        model = DoctorCharges
        fields = ['category', 'currency', 'price', 'desc_en', 'desc_yue', 'note_en', 'note_yue']


class DoctorAddressLanguageSerializer(serializers.ModelSerializer):
    """
    Doctor Address Language Serializer
    """

    class Meta:
        model = DoctorAddressLanguage
        fields = ['bcp47', 'address']


class DoctorOpeningHoursSerializer(serializers.ModelSerializer):
    """
    Doctor Opening Hours Serializer
    """

    class Meta:
        model = DoctorOpeningHours
        fields = ['day', 'open', 'close']


class DoctorSerializer(serializers.ModelSerializer):
    """
    Doctor serializer
    """

    opening_hours = DoctorOpeningHoursSerializer(many=True, read_only=True)
    charges = DoctorChargesSerializer(many=True, read_only=True)
    addresses = DoctorAddressLanguageSerializer(many=True, read_only=True)
    languages = serializers.SlugRelatedField(many=True, read_only=True, slug_field='bcp47')


    class Meta:
        model = Doctor
        fields = ['name', 'tel', 'district', 'open_public_holidays', 'languages',
        'opening_hours', 'charges', 'addresses']
