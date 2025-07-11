from django.shortcuts import render, HttpResponse
import random

def test(request):
     return HttpResponse(f"Hello World! {random.randint(1, 100)}")

def html_view(request):
     return render(request, "base.html")

