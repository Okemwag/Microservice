from django import forms
from suggestions.tasks import send_email_task_message

class SuggestionForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    suggestion = forms.CharField(
        label='Your suggestion',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))

    def send_email(self):
        send_email_task_message.delay(
             self.cleaned_data['name'],
             self.cleaned_data['email'],
             self.cleaned_data['suggestion']
        )
        
       