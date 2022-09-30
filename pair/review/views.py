from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Review
import random

# Create your views here.
def index(request):
    img_list = [
        "https://static.wikia.nocookie.net/pokemon/images/5/52/%ED%94%BC%EC%B9%B4%EC%B8%84_%EA%B3%B5%EC%8B%9D_%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8.png/revision/latest/scale-to-width-down/200?cb=20170405000019&path-prefix=ko",
        "https://static.wikia.nocookie.net/pokemon/images/3/3f/%EC%9D%B4%EB%B8%8C%EC%9D%B4_%EA%B3%B5%EC%8B%9D_%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8.png/revision/latest/scale-to-width-down/200?cb=20170405085011&path-prefix=ko",
        "https://static.wikia.nocookie.net/pokemon/images/c/c8/%EB%A6%AC%EC%9E%90%EB%AA%BD_%EA%B3%B5%EC%8B%9D_%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8.png/revision/latest/scale-to-width-down/250?cb=20170404233220&path-prefix=ko",
    ]

    review = Review.objects.all()
    count = Review.objects.count()
    images = []

    image = random.choice(img_list)

    context = {
        "reviews": review,
        "image": image,
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
