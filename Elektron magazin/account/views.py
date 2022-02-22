from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from account.models import Customer


def log_in(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', None)
        password = request.POST.get('password', None)
        customer = authenticate(request, phone_number=phone_number, password=password)
        if customer:
            login(request, customer)
            return redirect('home')

    return render(
        request=request,
        template_name='auth/signin.html'
    )


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('register')


def register(request):
    print(request.POST)
    user_message: str = ''
    password_message: str = ''
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        phone_number = request.POST.get('phone_number', None)
        password = request.POST.get('password', None)
        password1 = request.POST.get('password1', None)
        gender = request.POST.get('gender', None)
        user: Customer = Customer.objects.filter(phone_number=phone_number)
        if user:
            user_message = 'Raqam oldin kiritilgan'
        elif password1 != password:
            password_message = 'Plase make sure password fields is same'
        else:
            user = Customer.objects.create(
                last_name=last_name,
                first_name=first_name,
                phone_number=phone_number,
                password=password,
                gender=gender,
            )
            user.set_password(password)
            user.save()
            if user:
                login(request, user)
            return redirect('home')

    return render(
        request=request,
        template_name='auth/signup.html',
        context={
            'user_message': user_message,
            'password_message': password_message
        }
    )
