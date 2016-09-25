# coding: utf-8
from django import forms
from form.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name','email','message','subject', 'book')

class FeedbackForm2(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Full Name','id':'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Valid Email Address','id':'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message to Us','id':'message'}))
    subject = forms.ChoiceField(choices = ((1,'sffg'), (2,'dghhh')))

