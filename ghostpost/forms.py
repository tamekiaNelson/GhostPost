from django import forms


class RoastorBoastAddForm(forms.Form):
    Boast = forms.BooleanField()
    Roast = forms.BooleanField()
    post = forms.CharField(max_length=280)
    title = forms.CharField(max_length=100)
    up_votes = forms.IntegerField()
    down_votes = forms.IntegerField()
    submission_time = forms.TimeField()
