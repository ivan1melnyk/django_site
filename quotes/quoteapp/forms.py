from django import forms
from .models import Tag, Quote, Author


class TagForm(forms.ModelForm):

    name = forms.CharField(min_length=3, max_length=25,
                           required=True, widget=forms.TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(forms.ModelForm):

    name = forms.CharField(min_length=5, max_length=80,
                           required=True, widget=forms.TextInput())
    born_date = forms.DateField(widget=forms.DateInput())
    born_place = forms.CharField(min_length=5, max_length=150,
                                 required=True, widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Author
        fields = ['name', 'born_date', 'born_place', 'description']


class QuoteForm(forms.ModelForm):

    quote = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    # created = DateTimeInput()

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']
