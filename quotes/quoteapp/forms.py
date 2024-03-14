from django.forms import ModelForm, CharField, TextInput, Textarea, DateField, DateTimeInput
from .models import Tag, Quote, Author


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25,
                     required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):

    name = CharField(min_length=5, max_length=80,
                     required=True, widget=TextInput())
    born_date = DateField()
    born_place = CharField(min_length=5, max_length=150,
                           required=True, widget=TextInput())
    description = CharField(widget=Textarea)

    class Meta:
        model = Author
        fields = ['name', 'born_date', 'born_place', 'description']


class QuoteForm(ModelForm):

    quote = TextInput()
    # created = DateTimeInput()

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['author', 'tags']
