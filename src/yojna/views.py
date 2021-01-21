from django.shortcuts import render

# Create your views here.
def yojnahome(request):
    return render(request, 'yojna/yojna_home.html', {})