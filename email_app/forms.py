# email_app/forms.py
from django import forms
from .models import EmailInfo
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class EmailForm(forms.ModelForm):
    message_content = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class': 'w-full p-2 border rounded-md'}))

    class Meta:
        model = EmailInfo
        fields = ['to_email', 'company_name', 'purpose', 'message_content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full p-2 border rounded-md'

        self.fields['to_email'].widget.attrs['class'] += ' mb-4'
        self.fields['company_name'].widget.attrs['class'] += ' mb-4'
        self.fields['purpose'].widget.attrs['class'] += ' mb-4'
