from django.urls import path
from .views import base_views, answer_views, question_views, comment_views, vote_views

# 네임스페이스 지정
app_name = "board"

urlpatterns = [
    path("", base_views.index, name="index"),
    # 질문 생성
    path("<int:question_id>", base_views.detail, name="detail"),
    # /board/question/create/ question_create
    path("question/create/", question_views.question_create, name="question_create"),
    # /board/question/modify/305
    path(
        "question/modify/<int:question_id>",
        question_views.question_modify,
        name="question_modify",
    ),
    # /board/question/delete/305
    path(
        "question/delete/<int:question_id>",
        question_views.question_delete,
        name="question_delete",
    ),
    # 질문 답변 생성
    # /board/answer/create/1
    path(
        "answer/create/<int:question_id>",
        answer_views.answer_create,
        name="answer_create",
    ),
    # /board/answer/modify/1
    path(
        "answer/modify/<int:answer_id>",
        answer_views.answer_modify,
        name="answer_modify",
    ),
    # /board/answer/delete/1
    path(
        "answer/delete/<int:answer_id>",
        answer_views.answer_delete,
        name="answer_delete",
    ),
    # 질문 댓글 생성
    # /board/comment/create/question_id
    path(
        "comment/create/<int:question_id>",
        comment_views.comment_create_question,
        name="comment_create_question",
    ),
    path(
        "comment/modify/<int:comment_id>",
        comment_views.comment_modify_question,
        name="comment_modify_question",
    ),
    path(
        "comment/delete/<int:comment_id>",
        comment_views.comment_delete_question,
        name="comment_delete_question",
    ),
    # 답변 댓글 생성
    path(
        "comment/create_answer/<int:answer_id>",
        comment_views.comment_create_answer,
        name="comment_create_answer",
    ),
    path(
        "comment/modify_answer/<int:comment_id>",
        comment_views.comment_modify_answer,
        name="comment_modify_answer",
    ),
    path(
        "comment/delete_answer/<int:comment_id>",
        comment_views.comment_delete_answer,
        name="comment_delete_answer",
    ),
    path(
        "vote/question/<int:question_id>",
        vote_views.vote_question,
        name="vote_question",
    ),
    path(
        "vote/answer/<int:answer_id>",
        vote_views.vote_answer,
        name="vote_answer",
    ),
]
