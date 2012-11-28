# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from personalRecords.models import PersonalRecord
from personalRecords.entryForm import entryForm

import logging
logger = logging.getLogger('personalRecords')

def index(request):
    records = PersonalRecord.objects.all()
    context = { 'records': records }
    if request.method == 'POST':
        form = entryForm(request.POST)
        if form.is_valid():
#            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            p = PersonalRecord(first_name=first_name, last_name=last_name,
                address=address, city=city, state=state, zip_code=zip_code,
                email=email, phone=phone)
            p.save()
#        return HttpResponse("super")
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)

def detail(request, record_id):
    record = PersonalRecord.objects.get(id=record_id)
    context = {
        'first_name': record.first_name,
        'last_name': record.last_name,
        'address': record.address,
        'city': record.city,
        'state': record.state,
        'zip_code': record.zip_code,
        'email': record.email,
        'phone': record.phone,
    }
    return render(request, 'record_detail.html', context)

def form(request):
    form = entryForm()
    return render(request, 'form.html', {
        'form': form,
    })

def form_submit(request):
#    return HttpResponse("This is a response for form submission")
    if request.method == 'POST':
        print('woot')
        form = entryForm(request.POST)
        if form.is_valid():
#             logger.log(form.cleaned_data)
            print('yey')
