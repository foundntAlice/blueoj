from django import forms

class CodeSubmissionForm(forms.Form):
    problem_id = forms.IntegerField(widget=forms.HiddenInput())
    code = forms.CharField(widget=forms.Textarea)
