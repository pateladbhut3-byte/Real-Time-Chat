from django.forms import ModelForm
from django import forms
from .models import Groupmessage

class ChatmessageCreateFrom(ModelForm):
    class Meta:
        model = Groupmessage
        fields = ['body', 'file']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add message...',
                'class': 'py-2 px-3 w-full rounded-2xl bg-white text-black text-sm md:text-sm lg:text-sm',
                'maxlength': '300',
                'autofocus': True,
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'mt-2 w-full text-sm text-white file:bg-slate-700 file:text-white file:py-2 file:px-3 file:rounded-lg',
            }),
        }
