from django.views.generic.edit import FormView

from hierarchical_data.forms import AddFileForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = AddFileForm
    