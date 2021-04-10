"""
Models of Doctors Service
"""
from django.db import models


CATEGORIES = [
    ('d', 'Dentist'),
    ('cm', 'Chinese Medicine'),
    ('a', 'Acupuncture'),
    ('c', 'Chiropractor')
]

# 18 areas
DISTRICTS = [
    ('CW', 'Central and Western'),
    ('E', 'Eastern'),
    ('S', 'Southern'),
    ('WC', 'Wan Chai'),
    ('SSP', 'Sham Shui Po'),
    ('KC', 'Kowloon City'),
    ('KWT', 'Kwun Tong'),
    ('WTS', 'Wong Tai Sin'),
    ('YTM', 'Yau Tsim Wong'),
    ('I', 'Islands'),
    ('KTS', 'Kwai Tsing'),
    ('N', 'North'),
    ('SK', 'Sai Kung'),
    ('ST', 'Sha Tin'),
    ('TP', 'Tai Po'),
    ('TW', 'Tsuen Wan'),
    ('TM', 'Tuen Mun'),
    ('YL', 'Yuen Long')
]


class Doctor(models.Model):
    name = models.CharField(max_length=256)
    tel = models.CharField(max_length=256)
    district = models.CharField(choices=DISTRICTS, max_length=256)
    open_public_holidays = models.BooleanField(default=True)


class DoctorOpeningHours(models.Model):
    DAYS_OF_THE_WEEK = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday')
    ]
    doctor = models.ForeignKey(Doctor, related_name='opening_hours', on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_THE_WEEK)
    open = models.TimeField()
    close = models.TimeField()


class DoctorCharges(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='charges', on_delete=models.CASCADE)
    category = models.TextField(choices=CATEGORIES, max_length=256)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.TextField(max_length=3) # currency code ISO 4217
    desc_en = models.TextField(max_length=256)
    desc_yue = models.TextField(max_length=256)
    note_en = models.TextField(max_length=256)
    note_yue = models.TextField(max_length=256)


class DoctorLanguage(models.Model):
    """
    Doctor's language assignment, there's imperfection to this model, as there is
    an extra PK column, because we're not able to set a composite PK, ideally the
    doctor_language constraint should be the primary key
    """

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['doctor', 'bcp47'], name = 'doctor_language')
        ]

    doctor = models.ForeignKey(Doctor, related_name='languages',
        on_delete=models.CASCADE)
    bcp47 = models.CharField(max_length=256) # language tag following BCP 47 standard


class DoctorAddressLanguage(models.Model):
    """
    Doctor's address in different languages, similar imperfection due to lack of composite PK
    """

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['doctor', 'bcp47'], name = 'doctor_address_language')
        ]


    doctor = models.ForeignKey(Doctor, related_name='addresses', on_delete=models.CASCADE)
    bcp47 = models.CharField(max_length=256) # language tag following BCP 47 standard
    address = models.CharField(max_length=512)
