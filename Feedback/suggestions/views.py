from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from suggestions.forms import SuggestionForm

class SuggestionFormView(FormView):
    template_name = 'suggestions/suggestion.html'
    form_class = SuggestionForm
    success_url = '/suggestion/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(SuggestionFormView, self).form_valid(form)

class ThanksView(TemplateView):
    template_name = 'suggestions/thanks.html'

