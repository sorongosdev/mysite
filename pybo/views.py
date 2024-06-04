from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm

def index(request): # view 파일에 요청이 들어오면
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 기본키(pk)로  question_id를쓰겠다
    context = {'question': question}
    return render(request, 'pybo/question_detail.html',context)

def answer_create(request,  question_id):
    """ pybo 답변등록"""
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail',  question_id=question.id)

def question_create(request):
    if request.method == 'POST':    # 요청이 post 방식이면
        form = QuestionForm(request.POST)
        if form.is_valid():     # 폼이 유효하다면
            # commit 없이 form.save()를 수행하면 Question 모델의 create_date에 값이 설정되지 않아 오류가 발생할 것임
            # 임시 저장하여 question 객체를 리턴
            question = form.save(commit=False)
            question.create_date = timezone.now()   # 실제 저장을 위해 작성일시를 설정
            question.save()     # 실제로 데이터를 저장
            return redirect('pybo:index')   # pybo:index 로 이동, 실주소는 .../pybo/
    else:   # 요청이 post 방식이 아니라 get 방식이면
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html',context)
