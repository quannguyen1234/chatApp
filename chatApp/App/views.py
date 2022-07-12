from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from Room.models import Room,HistoryChatApp,Message
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def app(request):
    return render(request,"app.html")

@login_required(login_url='/accounts/login/')
def sendId(request):
    print(request.POST)
    url=reverse("boxchat",args=[request.POST['id']])
    return redirect(url)

@login_required(login_url='/accounts/login/')
def boxchat(request,id):
    tutorial = request.COOKIES
    room=None
    try:
        room=Room.objects.get(id=id)
    except:
        return HttpResponse("ko co phong")
    histories=HistoryChatApp.objects.filter(room=Room.objects.get(id=id))
    return render(request,"boxchat.html",{'room':room,'histories':histories})

@login_required(login_url='/accounts/login/')
def send_message(request):
    message=request.POST.get('message')
    mess=Message.objects.create(
        content=message
    )
    HistoryChatApp.objects.create(
        room=Room.objects.get(id=request.POST.get('room')),
        user=request.user,
        message=mess
    )
    return redirect(reverse('boxchat',args=[request.POST.get('room')]))

@login_required(login_url='/accounts/login/')
def lobby(request):
    return render(request,"lobby.html")
    