# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from personalRecords.models import PersonalRecord

def index(request):
#    return HttpResponse("This is the personal records page")
    records = PersonalRecord.objects.all()
    context = { 'records': records }
    return render(request, 'index.html', context)

def detail(request, record_id):
#    return HttpResponse("This is personal record with id %s." % record_id
    record = PersonalRecord.objects.get(id=record_id)
    context = {
        'first_name': record.first_name,
        'last_name': record.last_name,
        'address': record.address,
        'city': record.city,
        'state': record.state,
        'zip_code': record.zip_code
    }
    return render(request, 'record_detail.html', context)

def form(request):
#    return render(request, 'form_entry.html')
    form = entryForm()
    return render(request, 'form.html', {
        'form': form,
    })

def form_submit(request):
    return HttpResponse("This is a response for form submission")
