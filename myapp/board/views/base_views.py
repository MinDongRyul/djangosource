from django.shortcuts import get_object_or_404, render
from ..models import Question, QuestionCount
from django.core.paginator import Paginator
from django.db.models import Q, Count
from tools.utils import get_client_ip


def index(request):
    """
    질문목록
    """
    # return HttpResponse("Board")

    # question 테이블 내용 조회
    # Question.objects.all()

    page = request.GET.get("page", 1)  # http://127.0.0.1:8000/board/?page=1
    keyword = request.GET.get("keyword", "")
    sort = request.GET.get("sort", "")

    # 날짜 최신순으로 목록 조회
    # question_list = Question.objects.order_by("-create_date")

    # annotate() : voter라는 필드의 개수를 센 후 num_vorter라는 임시 필드를 추가해 주는 함수
    if sort == "recent":
        question_list = Question.objects.order_by("-create_date")
    elif sort == "recommend":
        question_list = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "-create_date"
        )

    elif sort == "popular":  # 인기순(답변이 많은)
        question_list = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-create_date"
        )
    else:
        question_list = Question.objects.order_by("-create_date")

    # 조회된 목록을 기준으로 검색 조건을 줘서 필터링
    # Q() : OR 조건으로 데이터를 조회
    # subject__contains(대소문자 구별)
    # subject__icontains(대소문자 구별 하지 않음)
    if keyword:
        question_list = question_list.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()

    paginator = Paginator(
        question_list, 10
    )  # Paginator 객체 생성(전체목록, 10) 전체목록에서 10개씩 가져오기
    page_obj = paginator.get_page(page)

    context = {
        "question_list": page_obj,
        "page": page,
        "keyword": keyword,
        "sort": sort,
    }

    return render(request, "board/question_list.html", context)


def detail(request, question_id):
    """
    질문 상세 조회
    """
    # 없는 id를 요청했을 때 웹 페이지에 오류 메세지가 그대로 출력
    # question = Question.objects.get(id=question_id)

    # Question에서 id = question_id인 데이터를 가져옴
    question = get_object_or_404(Question, id=question_id)

    # 페이지 나누기 추가
    page = request.GET.get("page", "")  # http://127.0.0.1:8000/board/?page=1
    keyword = request.GET.get("keyword", "")
    sort = request.GET.get("sort", "")

    # 조회수 추가
    # 사용자 ip 가져오기
    ip = get_client_ip(request)
    # 찾은 ip가 QuestionCount 테이블에 있는지 확인
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:  # 조회수 증가
        # 모델 생성
        qc = QuestionCount(ip=ip, question=question)
        # 저장
        qc.save()
        # question 테이블에 view_cnt = view_cnt + 1
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    context = {"question": question, "keyword": keyword, "sort": sort, "page": page}

    return render(request, "board/question_detail.html", context)
