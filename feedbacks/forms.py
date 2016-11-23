from django import forms

class FeedbackForm(forms.Form):
	his_name = forms.CharField(label='Name')
	his_feedback = forms.CharField(label='Feedback', widget=forms.Textarea)
