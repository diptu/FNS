from django.db import models
from bookings.models import Booking


class Transaction(models.Model):
	booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
	trs_id = models.CharField(max_length=64)
	amount = models.FloatField()
	transaction_datetime = models.DateTimeField()
	status = models.CharField(max_length=64)

	def __str__(self):
		return self.booking
