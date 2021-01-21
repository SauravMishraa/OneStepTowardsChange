from django.shortcuts import render

# Create your views here.
def publicnewshome(request):
    return render(request, 'publicnews/publicnews_home.html', {})