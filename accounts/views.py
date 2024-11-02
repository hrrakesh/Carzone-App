from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages,auth

from django.contrib.auth.models import User

from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
       
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')

        else:
            messages.warning(request, 'Invalid Credetials')
            return redirect('login')


    return render(request,'accounts/login.html')



def register(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if confirm_password == password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('register')

            # Create the user with automatic password hashing
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)

            # Log the user in
            #auth.login(request, user)

            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to dashboard after registration
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
    return render(request,'accounts/register.html')

def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You have Successfully logged out !')
        return redirect('home')

    return redirect('home')


@login_required(login_url = 'login')
def dashboard(request):
    
    user_inquiry = Contact.objects.filter(user_id=request.user.id, responded_view=True).order_by('-created_date')  # Corrected the method name to `filter`
    data = {
        'user_inquiry': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)
        
    

