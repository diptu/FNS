from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, FormView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from bookings.models import Booking
from properties.models import Ad
from django.contrib.auth import logout
from bookings.forms import BookingForm


class BookingView(LoginRequiredMixin, FormView, DetailView):
    # model         = Booking
    template_name = 'bookings/booking.html'
    form_class    = BookingForm
    success_url   = '/'

    def form_valid(self, form):
        if form.is_valid():
            #booking       = booking.objects.get(id = self.kwargs.get('id'))
            ad            = Ad.objects.get(slug = self.kwargs.get('slug'))
            guest         = self.request.user
            check_in      = form.cleaned_data.get('check_in')
            check_out     = form.cleaned_data.get('check_out')
            Booking.objects.create(ad=ad, guest=guest, check_in = check_in, check_out=check_out)
        return redirect('/')

    def get_object(self, *args, **kwargs):
        context = Ad.objects.get(slug = self.kwargs.get('slug'))
        print(context.title)
        return context
