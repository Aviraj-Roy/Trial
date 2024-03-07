from django.shortcuts import render,redirect
from app.models import Userdetails
from app.forms import UserInfo

# Create your views here.

def index(request):
    return render(request, "index.html")


def success(request):
    return render(request, "success.html")


############____ CRUD for ADMIN USERINFO _____#############


def insert(request):
    if request.method == "POST":
        form = UserInfo(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('registered')

            except:
                pass
    else:
        form = UserInfo()
    return render(request, 'success.html', {'form': form})


def show(request):
    userdetails = Userdetails.objects.all()
    return render(request, "userdetails.html", {'userdetails': userdetails})


def edit(request, id):
    userinfo = Userdetails.objects.get(id=id)
    return render(request, 'edit.html', {'userinfo': userinfo})


def update(request, id):
    userinfo = Userdetails.objects.get(id=id)
    form = UserInfo(request.POST, instance=userinfo)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request, 'edit.html', {'userinfo': userinfo})


def destroy(request, id):
    userinfo = Userdetails.objects.get(id=id)
    userinfo.delete()
    return redirect("show")
