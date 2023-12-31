from crispy_forms.layout import Submit
from django import forms
from crispy_forms.helper import FormHelper

from catalog.models import Product, Version



class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))



class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_of_creation', 'date_of_last_changing', 'version_number', 'owner')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_list = ['планшеты', 'плита', 'озеро', 'шлакоблоки', 'вереск', 'габилен', 'ель', 'оппонент',
                           'кантробас']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен к продаже")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        prohibited_list = ['планшеты', 'плита', 'озеро', 'шлакоблоки', 'вереск', 'габилен', 'ель', 'оппонент',
                           'кантробас']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен к продаже")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    ACTIVE_VERSIONS = []

    class Meta:
        model = Version
        fields = '__all__'
