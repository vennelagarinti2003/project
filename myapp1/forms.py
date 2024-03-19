from django import forms
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout


class hospitalregisterform(forms.ModelForm):
      class Meta:
            model=hospitalregistermodel
            fields='__all__'
      def save(self):
            s=super().save(commit=False)
            s.password=make_password(self.cleaned_data['password'])
            s.save()
            return s


class hospitalloginform(forms.ModelForm):
      class Meta:
            model=hospitalloginmodel
            fields='__all__'