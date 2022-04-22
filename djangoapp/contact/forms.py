from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(
        widget=forms.Textarea({"rows": 3}),
        help_text="You can message me about anything you want. "
        "Except chimeras. I hate chimeras.",
    )
    sender = forms.EmailField()

    def clean_message(self):
        # Accept any message, unless it contains the word 'chimera'
        message = self.cleaned_data["message"]
        if "chimera" in message.lower():
            raise forms.ValidationError("What did I tell you about chimeras?!")
        return message
