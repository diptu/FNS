from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView ,UpdateView , DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from properties.models import Ad
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout

class AdDelete(LoginRequiredMixin ,DeleteView):
    model   =   Ad
    success_url = '/properties/'



class AdUpdate(SuccessMessageMixin,LoginRequiredMixin ,UpdateView):
    model = Ad
    fields = ['title','content','image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        slug = self.object.slug
        #print(id)
        success_url = '/properties/'+str(slug)+'/'

        return  success_url

class AdDetailView(DetailView):
    model = Ad
    template = "properties/ad_detail.html"


class AdListView(ListView):
    model   =   Ad
    paginate_by = 3

class AdCreate(SuccessMessageMixin,LoginRequiredMixin ,CreateView):
    model = Ad
    fields = ['title','content','image']
    success_url = '/properties/'
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(AdCreate, self).form_valid(form)
