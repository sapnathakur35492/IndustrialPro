from django import forms
from .models import RFQRequest, Inquiry

class RFQForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty")

    class Meta:
        model = RFQRequest
        fields = ['name', 'company_name', 'email', 'phone', 'country', 'product_requirement', 'material_requirement', 'quantity', 'message', 'file_upload']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'product_requirement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Required'}),
            'material_requirement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material (e.g. Stainless Steel)'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity Needed'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Additional Message'}),
            'file_upload': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_file_upload(self):
        file = self.cleaned_data.get('file_upload')
        if file:
            if file.size > 20 * 1024 * 1024:
                raise forms.ValidationError('File size must be under 20MB.')
        return file

    def clean_honeypot(self):
        honeypot = self.cleaned_data.get('honeypot')
        if honeypot:
            raise forms.ValidationError('Invalid submission.')
        return honeypot

class InquiryForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty")

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'product_name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_honeypot(self):
        honeypot = self.cleaned_data.get('honeypot')
        if honeypot:
            raise forms.ValidationError('Invalid submission.')
        return honeypot
