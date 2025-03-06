from django.shortcuts import render
from . models import movieinfo
from . forms import movieinfoForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def create(request):
    frm=movieinfoForm()
    if request.POST:
        frm=movieinfoForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
    else:
        frm=movieinfoForm()
    return render(request, "create.html",{"frm":frm})

def list(request):
    movieset = movieinfo.objects.all()
    print(movieset)
    return render(request, "list.html",{'movies':movieset})

def edit(request,pk):
    instancetbd = movieinfo.objects.get(pk=pk)
    if request.POST:
        frm = movieinfoForm(request.POST,instance=instancetbd)
        if frm.is_valid():
            frm.save()
    else:        
        frm = movieinfoForm(instance=instancetbd)
    return render(request, "create.html",{"frm":frm})

def delete(request,pk):
    instance=movieinfo.objects.get(pk=pk)
    instance.delete()
    movieset = movieinfo.objects.all()
    return render(request, "list.html",{'movies':movieset})


