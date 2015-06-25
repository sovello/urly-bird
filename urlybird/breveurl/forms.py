from django import forms
from breveurl.bookmark import Bookmark
from django.contrib.auth.models import User


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('url', 'description', 'tag')
        widgets = {}

        widgets = {
'photo' : forms.ClearableFileInput(attrs={'accept': 'image/*', 'name':'image'}),
            }
    #fields = ('occupation', 'age', 'zip_code', 'photo')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['rating']

        
class ContactForm(forms.Form):
    name = forms.CharField(label = "Your Name", max_length = 255)
    subject = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

