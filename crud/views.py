from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile


# Create your views here.

def First(request):
    if request.method == 'get':
        user_prof = Profile.GET.get('search')
        print(user_prof)
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
