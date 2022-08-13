from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .forms import PhotoForm
from .models import Photo


def photo_list(request):
    # 텍스트 보여주기
    # return HttpResponse("Hello Photo")

    # 특정 templates 보여주기
    # render() : 특정 템플릿 파일을 이용해서 views 지정하고
    #            데이터베이스 내용을 보낼 수 있음

    # Photo.objects.all() : Photo 테이블 내용 전체조회

    photos = Photo.objects.all()

    return render(request, "photo/photo_list.html", {"photos": photos})


def photo_detail(request, pk):
    # pk에 해당하는 데이터를 찾아보고 있으면 Photo 에 담고
    # 없으면 404 반환
    photo = get_object_or_404(Photo, pk=pk)

    return render(request, "photo/photo_detail.html", {"photo": photo})


def photo_post(request):

    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()  # db에 insert
            return redirect("photo_detail", pk=photo.pk)
    else:  # get 방식으로 요청 : 비어 있는 폼 전송
        form = PhotoForm()

    return render(request, "photo/photo_post.html", {"form": form})


def photo_edit(request, pk):

    # pk에 해당하는 내용 찾아오기
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect("photo_detail", pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)

    return render(request, "photo/photo_post.html", {"form": form})


def photo_remove(request, pk):
    # pk 에 해당하는 사진 찾기
    photo = get_object_or_404(Photo, pk=pk)

    # 삭제
    photo.delete()
    # 삭제 후 이동할 경로
    return redirect("photo_list")
