# Create your models here.
from django.db import models
from django.urls import reverse

class Table(models.Model):
    name = models.CharField(max_length=255)

    # Metadata
    class Meta:
        ordering = ['name']


class Reservation(models.Model):

    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    date = models.DateField()

    time = models.TimeField()

    canceled = models.BooleanField(default=False)

 
    """A typical class defining a model, derived from the Model class."""

# Metadata

    class Meta:

        ordering = ['-date', 'name']

    

 

    # Methods

    def get_absolute_url(self):

        """Returns the URL to access a particular instance of MyModelName."""

        return reverse('reservation_detail', args=[str(self.id)])

 

    def __str__(self):

        """String for representing the MyModelName object (in Admin site etc.)."""

        return self.name

 

    def cancel(self):

        self.canceled = True

        self.save()