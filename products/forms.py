from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'form-control'})
        self.fields['hunter'].widget.choices = [('', 'Select Hunter'), ] + list(self.fields['hunter'].widget.choices)[1:]
    
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['pub_date', 'votes_total']
        widgets = {
            'url': forms.TextInput()
        }
        error_messages = {
            'title': {
                'required': 'Title is Required'
            },
            'url': {
                'required': 'Url is Required'
            },
            'image': {
                'required': 'Image is Required'
            },
            'icon': {
                'required': 'Icon is Required'
            },
            'body': {
                'required': 'Body is Required'
            },
            'hunter': {
                'required': 'Please select Hunter'
            },
        }

