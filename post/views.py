from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Volunteer
from .forms import CreatePostForm
# Create your views here.

def home(request):
    person = Volunteer.objects
    return render(request,'home.html',{'person':person})

def detail(request,volunteer_id):
    volunteer_detail = get_object_or_404(Volunteer, pk=volunteer_id)
    return render(request,'detail.html',{'volunteer_detail':volunteer_detail})

def apply(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.date = timezone.datetime.now()
            volunteer.save()
        return redirect('/detail/'+str(volunteer.id))
    else:  
        form = CreatePostForm()
    return render(request,'apply.html',{'form':form})

def update(request,volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    if request.method == "POST":
        form = CreatePostForm(request.POST,instance=volunteer)
        if form.is_valid():
            volunteer = form.save()
            return redirect('/detail/'+str(volunteer.id))
    else:
        form = CreatePostForm(instance=volunteer)
        return render(request,'apply.html',{'form':form})

def delete(request,volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    volunteer.delete()
    return redirect('home')