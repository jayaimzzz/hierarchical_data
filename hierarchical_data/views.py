from django.views import View
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from hierarchical_data.forms import AddFileForm
from hierarchical_data.models import File

class IndexView(View):
    template = 'index.html'
    def get(self, request):
        data = {
            'files': File.objects.all()
        }
        return render(request, self.template, data)


class AddFileView(FormView):
    template_name= 'add_file.html'
    form_class = AddFileForm
    def form_valid(self, form):
        data = form.cleaned_data
        file = File.objects.create(
            name=data['name'],
            parent=data['parent']
        )
        return HttpResponseRedirect(self.request.GET.get('next', '/'))

    

    