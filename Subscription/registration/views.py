from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from registration.forms import SubscriptionForm
from registration.models import Address


class SubscriptionFormView(FormView):
    template_name = "registration/subscription.html"
    form_class = SubscriptionForm
    success_url = "/success/"

    def form_valid(self, form):
        address = Address(
            name=form.cleaned_data["name"],
            address=form.cleaned_data["address"],
            postalcode=form.cleaned_data["postalcode"],
            city=form.cleaned_data["city"],
            country=form.cleaned_data["country"],
            email=form.cleaned_data["email"],
        )
        address.save()

        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "registration/success.html"
