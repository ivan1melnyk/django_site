from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Author, Quote
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.core.paginator import Paginator


# Create your views here.
def main(request):
    # if request.user.is_authenticated:
    quotes = Quote.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(quotes, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'quoteapp/index.html', {"page_obj": page_obj, "authors": authors, "tags": tags})


class AuthorView(DetailView):
    model = Author
    template_name = 'quoteapp/author.html'
    context_object_name = 'author'


def quotes_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    quotes = tag.quote_set.all()
    return render(request, 'quoteapp/quotes_by_tag.html', {'tag': tag, 'quotes': quotes})


@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/add_author.html', {'form': form})

    return render(request, 'quoteapp/add_author.html', {'form': AuthorForm()})


@login_required
def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user

            author_id = request.POST.get('author')
            author = get_object_or_404(Author, id=author_id)

            new_quote.author = author
            new_quote.save()

            tags_names = request.POST.getlist('tags')
            choice_tags = Tag.objects.filter(name__in=tags_names)
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, "authors": authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors": authors, 'form': QuoteForm()})


@login_required
def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, user=request.user)
    return render(request, 'quoteapp/detail.html', {"quote": quote})


@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quoteapp:main')
