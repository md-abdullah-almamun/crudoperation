from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.db.models import Q
import os


# Create your views here.

def First(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            user_prof = Profile.objects.filter(Q(name__icontains=search) | Q(Email__icontains=search))
            if not user_prof:
                messages.success(request, "No Such account Exists")
                return redirect('first')
        else:
            user_prof = Profile.objects.all()

    return render(request, 'First.html', locals())


def Create(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        gender = request.POST.get('gender')

        if name:
            if image:
                prof = Profile.objects.create(
                    name=name,
                    image=image,
                    Email=email,
                    age=age,
                    address=address,
                    phone_no=phone_no,
                    date_of_birth=date_of_birth,
                    religion=religion,
                    gender=gender,

                )
                prof.save()

                messages.success(request, "Profile details Create.")
                return redirect('first')

            else:
                prof = Profile.objects.create(
                    name=name,
                    Email=email,
                    age=age,
                    address=address,
                    phone_no=phone_no,
                    date_of_birth=date_of_birth,
                    religion=religion,
                    gender=gender,

                )
                prof.save()
                messages.success(request, "Profile details Create.")
                return redirect('first')
        else:
            messages.error(request, "Fill Up All Field")

    return render(request, 'create.html', locals())


def Delete(request, id):
    prof = Profile.objects.get(id=id)
    prof.delete()
    return redirect('first')


def see_Profile(request,id):
    prof = Profile.objects.get(id=id)
    return render(request,'SeeFullProfile.html',locals())


def update_prof(request,id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES.get('image')) != 0:
            if prof.image != 'default/def.jpg':
                os.remove(prof.image.path)
            else:
                pass
            prof.name = request.POST['name']
            prof.image = request.FILES.get('image')
            prof.email = request.POST.get('email')
            prof.age = request.POST.get('age')
            prof.address = request.POST.get('address')
            prof.phone_no = request.POST.get('phone_no')
            prof.date_of_birth = request.POST.get('date_of_birth')
            prof.religion = request.POST.get('religion')
            prof.gender = request.POST.get('gender')
            prof.save()
            messages.success(request, "Profile details Updated.")
            return redirect('first')
        else:
            prof.name = request.POST['name']
            prof.email = request.POST.get('email')
            prof.age = request.POST.get('age')
            prof.address = request.POST.get('address')
            prof.phone_no = request.POST.get('phone_no')
            prof.date_of_birth = request.POST.get('date_of_birth')
            prof.religion = request.POST.get('religion')
            prof.gender = request.POST.get('gender')
            prof.save()
            messages.success(request, "Profile details Updated.")
            return redirect('first')
    return render(request, 'update_prof.html', locals())
