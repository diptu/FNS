from django.db import models
from profiles.models import User
from properties.models import Ad

class Booking(models.Model):
	# PAYMENT_HISTORY = (
    #     (0, ("Unpaid")),
    #     (1, ("Paid")),
    # )
	ad 				 = models.ForeignKey(Ad, on_delete=models.CASCADE)
	guest 			 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')
	# payment_status	 = models.IntegerField(choices=PAYMENT_HISTORY, default=0)
	check_in		 = models.DateTimeField()
	check_out		 = models.DateTimeField()
	# timestamp  		 = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.guest.username
	# def __init__(self):
	# 	return self.ad.get(id=self.ad.id)
