from django.forms import ModelForm
from django import forms
from .models import GoalList, GoalModel

class GoalForm(ModelForm):
    
    class Meta:
        model = GoalList
        fields = ("goal",)
    
class GoalModelForm(ModelForm):
    class Meta:
        model = GoalModel
        fields = ('datetogoal',"is_true",)
   
    def save(self):
        data=self.cleaned_data
   
class GoalModelCheck(ModelForm):
    class Meta:
        model = GoalModel
        fields = ("is_true","datetogoal")


class GoalOrdinaryForm(forms.Form):
    is_true=forms.BooleanField(required=False )

class GoalOrdinaryFormFalse(forms.Form):
    is_not_true=forms.BooleanField(required=False)

class AccountabilityPartnerForm(forms.Form):
    first_name=forms.CharField( max_length=50)
    last_name=forms.CharField( max_length=50)
    email = forms.EmailField()
    phone_number=forms.IntegerField()


