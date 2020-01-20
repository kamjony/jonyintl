from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput())
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput())
    message = forms.CharField(
        max_length=2000,
        help_text='Write here your message!',
        widget=forms.Textarea()
    )
