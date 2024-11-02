from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact,NonCarContact
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        car_title = request.POST.get('car_title')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_need = request.POST.get('customer_need')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message_content = request.POST.get('message')  # Avoid conflict with Django messages module

        # Check for existing inquiry for authenticated users
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id)
            if has_contacted.exists():
                messages.error(request, 'You have already submitted an inquiry for this car. We will get back to you soon.')
                return redirect('/cars/' + car_id)

        # For non-authenticated users
        else:
            user_id = 0  # Set user_id to 0 for non-authenticated users
            has_contacted = Contact.objects.filter(car_id=car_id, email=email)
            if has_contacted.exists():
                messages.error(request, 'You have already submitted an inquiry for this car. We will get back to you soon.')
                return redirect('/cars/' + car_id)

        # Create and save the contact request
        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message_content
        )
        contact.save()

        # Send email notification
        try:
            send_mail(
                'New Car Inquiry',
                f"""
                Hi Rakesh,

                You have received a new inquiry regarding a car!

                Please log in to the admin panel to review the details.

                Inquiry Details:
                -----------------
                - **Car Name:** {car_title}
                - **User Email:** {email}
                - **Phone:** {phone}
                
                Customer Information:
                ----------------------
                - **User ID:** {user_id}
                - **First Name:** {first_name}
                - **Last Name:** {last_name}
                - **Customer Need:** {customer_need}
                
                Location:
                ----------
                - **City:** {city}
                - **State:** {state}

                Message:
                ----------
                {message_content}

                Thank you,
                Car Inquiry System @carzone
                """,
                'hello@gmail.com example',
                ['hi@gmail.com example'],
                fail_silently=False,
            )

        except Exception as e:
            messages.error(request, 'There was an issue sending the email. Please try again later.')

        messages.success(request, 'Your inquiry has been submitted. We will get back to you shortly.')
        return redirect('/cars/' + car_id)


def other_inquiry(request):
    if request.method == 'POST':
        
        full_name = request.POST.get('full_name')

        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')  # Avoid conflict with Django messages module

      
            
        has_contacted = NonCarContact.objects.filter(email=email)
        if has_contacted.exists():
            messages.error(request, 'You have already submitted an inquiry . We will get back to you soon.')
            return redirect('contact')

        # Create and save the contact request
        contact = NonCarContact(
            full_name = full_name,
    
            email = email,
            subject = subject,
            phone = phone,
            message = message
        )

        contact.save()

        # Send email notification
        try:
            send_mail(
                'New Contact Request!',
                f"""
                Hi Rakesh,

                You have a new contact request!

                Please log in to the admin panel to review it.

                Contact Details:
                -----------------
                - **User Email:** {email}
                - **Phone:** {phone}
                - **Name:** {full_name}
                - **Subject:** {subject}
                - **Message:** {message}

                Thank you,

                Your Carzone Contact System
                """,
                'hello@gmail.com example',
                ['hi@gmail.com example'],
                fail_silently=False,
            )

        except Exception as e:
            messages.error(request, 'There was an issue sending the email. Please try again later.')

        messages.success(request, 'Your inquiry has been submitted. We will get back to you shortly.')
        return redirect('contact')
