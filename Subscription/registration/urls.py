from django.urls import path

from registration.views import SubscriptionFormView, SuccessView

app_name = "subscription"

urlpatterns = [
    path("subscription/", SubscriptionFormView.as_view(), name="subscription"),
    path("success/", SuccessView.as_view(), name="success"),
]
