
from django import forms
from .models import Consultation, Register
class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = "__all__"



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
