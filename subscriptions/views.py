
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm
from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Check if the email already exists
            email = form.cleaned_data['email']
            if not Subscriber.objects.filter(email=email).exists():
                form.save()
                messages.success(request, 'You have successfully subscribed!')
            else:
                messages.info(request, 'This email is already subscribed.')
            return redirect('subscribe')
    else:
        form = SubscriberForm()
    return render(request, 'subscriptions/subscribe.html', {'form': form})
