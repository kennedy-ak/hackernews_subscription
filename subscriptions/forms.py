# subscriptions/forms.py
from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email','name','number']

# subscriptions/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have subscribed successfully!')
            return redirect('subscribe')
    else:
        form = SubscriberForm()
    return render(request, 'subscriptions/subscribe.html', {'form': form})
