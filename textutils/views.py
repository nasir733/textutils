# i have created this website -Nasir
from django.http import HttpResponse

# Code for video: 6
def index(request):
    return HttpResponse('''nasir  Django NasirIqbal''')

def about(request):
    return HttpResponse("About Nasir")