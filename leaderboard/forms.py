from django import forms 
from .models import Scorecard


class Enter_Score(forms.ModelForm):
    
    class Meta:
        model = Scorecard
        fields = ('name','score')
