from django import forms
from .models import Goal, DailyUpdate

class GoalForm(forms.ModelForm):
    is_shared = forms.BooleanField(required=False, label="Share with Partner")
    class Meta:
        model = Goal
        fields = ['title', 'description', 'deadline', 'penalty', 'is_shared']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class DailyUpdateForm(forms.ModelForm):
    class Meta:
        model = DailyUpdate
        fields = ['achievements', 'bottlenecks', 'plan_for_tomorrow', 'mood_rating']

class PartnerConnectionForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
