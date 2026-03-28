from django.shortcuts import render, redirect
from django.conf import settings
from .forms import InputForm
from datetime import datetime
import os

# Create your views here.
def index(request):
    history = []

    if os.path.exists(settings.LOG_FILE_PATH):
        with open(settings.LOG_FILE_PATH, 'r') as f:
            history = f.readlines()
    
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{timestamp} - {text}\n"

            with open(settings.LOG_FILE_PATH, 'a') as f:
                f.write(entry)

            return redirect('index')
    
    else:
        form = InputForm()

    return render(request, 'ex02/index.html', {
        'form': form,
        'history': history
    })