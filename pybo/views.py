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
    form = QuestionForm()
    return render(request, 'pybo/quesion_form.html',{'form':form})