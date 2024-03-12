from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import TagForm, QuoteForm
from .models import Tag, Author


# Create your views here.
def main(request):
    return render(request, 'quoteapp/index.html')


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(
                name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            choice_authors = Author.objects.filter(
                name__in=request.POST.getlist('authors'))
            for author in choice_authors.iterator():
                new_quote.authors.add(author)

            new_quote.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, "authors": authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors": authors, 'form': QuoteForm()})
