from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, 'name':"Let's Learn Python!"},
    {'id':2, 'name':"Let's Learn React JS!"},
    {'id':3, 'name':"Let's Learn Data Engineering!"}
]

# Create your views here.
def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    print(pk)
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = i 
    context = {"room":room}
    return render(request, 'base/room.html', context)