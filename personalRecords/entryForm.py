from django import forms

class entryForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)
    state = forms.CharField(max_length=50, required=False)
    zip_code = forms.IntegerField(required=False)
    email = forms.CharField(max_length=50, required=False)
    phone = forms.IntegerField()

