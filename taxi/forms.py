from typing import re

from django import forms
from .models import Driver, Car


class DriverLicenseForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError("License must be 8 characters long.")
        if not re.match(r"^[A-Z]{3}\d{5}$", license_number):
            raise forms.ValidationError("License must start with 3 uppercase letters followed by 5 digits.")
        return license_number


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["manufacturer", "drivers"]
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(),
        }
