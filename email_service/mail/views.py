from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import emailRecord
from .tasks import send_email_task

def initiateEmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        email_record, created = emailRecord.objects.get_or_create(email=email)
        if created:
            send_email_task.apply_async(args=[email_record.id], countdown=0)
        return redirect('initiateEmail')
    
    email_records = emailRecord.objects.all()

    return render(request, 'initiateEmail.html', {'email_records': email_records})
