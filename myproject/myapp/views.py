from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import MyModel

# Create your views here.

class MyView(View):
    def get(self, request):
        return HttpResponse("Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt repellat deleniti hic quasi atque beatae doloribus expedita autem voluptas pariatur.!")
    
class MyTemplateView(TemplateView):
    template_name = 'my_template.html'

class MyListView(ListView):
    model = MyModel
    template_name = 'my_list.html'
    context_object_name = 'my_objects'
