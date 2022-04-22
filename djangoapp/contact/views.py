from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm


def contact_form(request):
    if request.method == "POST":
        print(">" * 100)
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required and do something with it
            return render(request, "contact_form_confirm.html")
    else:
        form = ContactForm()

    return render(request, "contact_form.html", {"contact_form": form})
