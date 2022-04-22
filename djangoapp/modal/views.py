from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def simple_modal(request):
    return render(request, "simple_modal.html")
