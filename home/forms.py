from django import forms

class YouTubeForm(forms.Form):
    url = forms.URLField(label='YouTube URL', help_text='Enter a YouTube URL')
    
