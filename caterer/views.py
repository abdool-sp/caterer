from typing import Any, Dict
from django.shortcuts import render
from .models import Caterer,Service
from django.views.generic import ListView,DetailView


# Create your views here.

class CaterersListView(ListView):
    template_name = "caterer_page.html"
    model = Caterer


class CatererDetailView(DetailView):
    model = Caterer

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        caterer = context['object']
        services = caterer.service_set.all()
        context['services'] = services
        return context

def caterer_page(request):
    return render(request,template_name="caterer_page.html")
