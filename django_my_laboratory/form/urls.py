from django.urls import path
from form.views import post_model_formset

app_name = "form"

urlpatterns = [
    path("model_formset/", post_model_formset.add, name="post_model_formset"),
]
