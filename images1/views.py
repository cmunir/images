from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')
def gallery_view(request):
    return render(request,'gallery.html')
def contact_view(request):
    return render(request,'contact.html')
def services_view(request):
    return render(request,'services.html')
def feedback_view(request):
    return render(request,'feedback.html')
