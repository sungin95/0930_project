from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    review = Review.objects.all()
    context = {
        "reviews": review,
    }
    return render(request, "review/index.html", context)


def new(request):

    return render(request, "review/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(
        title=title,
        content=content,
    )

    return redirect("review:index")


def detail(request, pk_):
    review = Review.objects.get(pk=pk_)
    context = {
        "review_id": review,
    }

    return render(request, "review/detail.html", context)


def edit(request, pk_):
    review = Review.objects.get(pk=pk_)
    context = {
        "review_id": review,
    }
    return render(request, "review/edit.html", context)


def update(request, pk_):
    review = Review.objects.get(pk=pk_)
    update_title = request.GET.get("title")
    update_content = request.GET.get("content")
    review.title = update_title
    review.content = update_content
    review.save()
    return redirect("review:detail", review.pk)


def delete(request, pk_):
    review = Review.objects.get(pk=pk_)
    review.delete()
    return redirect("review:index")
