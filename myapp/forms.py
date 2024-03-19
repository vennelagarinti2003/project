from django import forms
from .models import patientregistermodel,patientloginmodel
from django.contrib.auth.hashers import make_password


class patientregisterform(forms.ModelForm): 
    class Meta: 
        model = patientregistermodel 
        fields = "__all__" 
    def save(self): 
        s=super().save(commit=False) 
        s.password=make_password(self.cleaned_data['password']) 
        s.save() 
        return s 
 
class patientloginform(forms.ModelForm): 
    class Meta: 
        model = patientloginmodel 
        fields = "__all__"


