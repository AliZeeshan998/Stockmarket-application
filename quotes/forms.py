from django import forms
from .models import Stock

class StockForm(forms.Form):
    class Meta:
        model = Stock
        fields = ["ticker"]
