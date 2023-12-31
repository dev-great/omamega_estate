from django.conf import settings
from django.db import models

from Property.choices import DOCUMENT_TYPE_CHOICES, PROPERTY_TYPE_CHOICES, STATES_CHOICES
from Tenant.models import Tenant
from cloudinary.models import CloudinaryField

# Create your models here.


class Document(models.Model):
    document_type = models.CharField(
        max_length=30, choices=DOCUMENT_TYPE_CHOICES)
    file = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file)

    class Meta:
        ordering = ['-updated_on']


class PropertyManager(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_information = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_on']


class PropertyImage(models.Model):
    image = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-updated_on']


class Property(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=255)
    state = models.CharField(
        max_length=50, choices=STATES_CHOICES, default='Abuja')
    property_type = models.CharField(
        max_length=15, choices=PROPERTY_TYPE_CHOICES)
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    parking = models.BooleanField(default=False)
    square_feet = models.PositiveIntegerField()
    year_built = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    documents = models.ManyToManyField(Document)
    property_manager = models.ForeignKey(
        PropertyManager, on_delete=models.SET_NULL, null=True)
    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_estate = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    tenants = models.ManyToManyField(Tenant, blank=True)
    images = models.ManyToManyField(PropertyImage)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_on']


class Subscriber(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=100, decimal_places=2)
    balance = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    plot_no = models.CharField(max_length=255)
    plot_size = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.email)

    class Meta:
        ordering = ['-updated_on']
