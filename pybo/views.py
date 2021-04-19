# view.py : 실제 그 리퀘스트를 던짐 받는 곳. 함수를 짜놓은 실제 로직부분이 있는 곳
# 따라서 여기에 어떤 요청을 받았는지 정확히 명시해줘야함 (get: db정보를 가져가기만 하고, post : db를 실제로 수정, 저장, 삭제 가능)
# 뷰 안에 있는 클래스의 이름은 그 기능을 직관적으로 알 수 있게끔 짜는 것이 중요
# HttpResponse : 별다른 메시지가 필요치 않을 때 JsonResponse : json데이터 형식으로 뭔가 메세지를 표현할 때 사용용
# ---------------------------------- [edit] ---------------------------------- #
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question
from django.utils import timezone
# ---------------------------------- [edit] ---------------------------------- #
from .forms import QuestionForm, AnswerForm
# ---------------------------------------------------------------------------- #
from django.core.paginator import Paginator

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

# ---------------------------------- [edit] ---------------------------------- #    
    return render(request, 'pybo/question_list1.html', context)
# ---------------------------------------------------------------------------- #

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk = question_id)
   # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # ---------------------------------- [edit] ---------------------------------- #
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


# ---------------------------------------------------------------------------- #

# ---------------------------------- [edit] ---------------------------------- #
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
# ---------------------------------------------------------------------------- #
