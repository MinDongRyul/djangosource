from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    # 문자열 보여주기
    # return HttpResponse("Todo 앱")
    # Todo.objects.all() # 전체 내용 가져오기

    # complete가 False 레코드 가져오기
    todos = Todo.objects.filter(complete=False)

    # 특정 html 파일 보여주기
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_detail(request, pk):
    # pk 에 해당하는 레코드 가져오기
    todo = Todo.objects.get(id=pk)
    return render(request, "todo/todo_detail.html", {"todo": todo})


def todo_register(request):
    """
    http://127.0.0.1:8000/todo/new 경로로 Get 요청,Post 요청
    """
    if request.method == "POST":
        form = TodoForm(request.POST)
        todo = form.save(commit=False)
        todo.save()
        # 입력 성공 후 가야할 곳
        return redirect("todo_detail", pk=todo.id)
    else:  # GET
        # todo 입력 가능한 폼 보여주기
        form = TodoForm()

    return render(request, "todo/todo_register.html", {"form": form})
