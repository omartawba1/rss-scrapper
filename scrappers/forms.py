from django import forms


class RSSPostForm(forms.Form):
    url = forms.URLField(required=True)
