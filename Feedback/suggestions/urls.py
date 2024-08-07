from django.urls import path
from .views import SuggestionFormView, ThanksView

urlpatterns = [
    path('suggestion', SuggestionFormView.as_view(), name='suggestion_form'),
    path('suggestion/thanks/', ThanksView.as_view(), name='thanks')
]