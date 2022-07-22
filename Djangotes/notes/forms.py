from django import forms

class LogInForm(forms.Form):
    user_id = forms.IntegerField(label="Log in as user")

class NoteForm(forms.Form):
    notetext = forms.CharField(widget=forms.Textarea, label="Notepad", max_length=500) # length is validated on django's side, too