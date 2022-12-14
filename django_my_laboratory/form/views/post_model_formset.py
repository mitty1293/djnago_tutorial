from django import forms
from django.shortcuts import redirect, render
from form.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


EmployeeFormset = forms.modelformset_factory(Employee, form=EmployeeForm, extra=1)


def add(request):
    formset = EmployeeFormset(request.POST or None)
    if request.method == "POST" and formset.is_valid():
        formset.save()
        return redirect("form:post_model_formset")
    context = {
        "formset": formset,
    }
    return render(request, "form/post_model_formset.html", context)
