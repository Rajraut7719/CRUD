from secrets import choice
from attr import attr
from django import forms
from .models import User



class StudentRegistration(forms.ModelForm):
    # Employee= forms.CharField(widget=forms.Select(choices=EMP_CHOICES))
    class Meta:
        model=User
        fields=['emp','title','email','description']
        widgets={
            'emp': forms.Select(attrs={'class':'form-control p-2 mt-2'}),
            'title':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control p-2 mt-2'}),
            'description':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),

        }
