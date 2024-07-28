# myapp/forms.py
from django import forms
from .models import Consumption, Item

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = ['item', 'quantity']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
