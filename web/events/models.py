from django.db import models
from django.urls import reverse


class Address(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def get_name(self):
        return self.name

    def get_street(self):
        return str(self.street)

    def get_street_number(self):
        return self.street_number

    def get_city(self):
        return str(self.city)

    def has_name(self):
        return (self.name is not None) and (self.name != "")

    def get_google_maps_link_for_street(self):
        return "http://maps.google.com/maps?q={} {}, {}".format(self.street, self.street_number, self.get_city())

    def get_google_maps_link_for_city(self):
        return "http://maps.google.com/maps?q={}".format(self.get_city())

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)

    from_date_time = models.DateTimeField()
    to_date_time = models.DateTimeField()
    title = models.CharField(max_length=80)
    contact_person = models.CharField(max_length=80, null=True, blank=True)

    def get_title(self):
        return self.title

    def get_from_date_time(self):
        return self.from_date_time

    def get_to_date_time(self):
        return self.to_date_time

    def get_date(self):
        return self.from_date_time.strftime("%d. %b %Y")

    def get_address(self):
        return self.address

    def get_detail_url(self):
        return reverse('events:detail', args=[ str(self.id), ])

    def has_contact_person(self):
        return self.contact_person is not None and self.contact_person != ""

    def get_contact_person(self):
        return self.contact_person

    def __str__(self):
        return str(self.title)
