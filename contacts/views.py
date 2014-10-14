from django.shortcuts import render
from django.views.generic import View

from .models import *

# Create your views here.
class IndexView(View):
    def get(self, *args, **kwargs):
        context = {}
        context['contacts'] = Contact.objects.all()

        return render(self.request, "base.html", context)