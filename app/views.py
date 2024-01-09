from django.shortcuts import render

# Create your views here.
def home(request):
    print('home page view')
    return render(request,'middleware/home.html')

def info(request):
    print('information page')
    return render(request,'middleware/info.html')