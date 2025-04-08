from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Survey, Question, Response, Answer

class SurveyListView(ListView):
    model = Survey
    template_name = 'polls/index.html'
    context_object_name = 'survey_list'
    ordering = ['-pub_date']

class SurveyDetailView(DetailView):
    model = Survey
    template_name = 'polls/detail.html'
    context_object_name = 'survey'

def survey_response(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    
    if request.method == 'POST':
        if 'nickname' in request.POST:
            # 닉네임 입력 처리
            nickname = request.POST['nickname']
            response = Response.objects.create(survey=survey, nickname=nickname)
            return redirect('polls:answer_questions', survey_id=survey_id, response_id=response.id)
        else:
            # 설문조사 응답 처리
            response_id = request.POST.get('response_id')
            response = get_object_or_404(Response, pk=response_id, survey=survey)
            
            for question in survey.questions.all():
                answer_text = request.POST.get(f'question_{question.id}')
                if answer_text:
                    Answer.objects.create(
                        response=response,
                        question=question,
                        answer_text=answer_text
                    )
            
            return redirect('polls:survey_complete', survey_id=survey_id)
    
    return render(request, 'polls/nickname_form.html', {'survey': survey})

def answer_questions(request, survey_id, response_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    response = get_object_or_404(Response, pk=response_id, survey=survey)
    
    if request.method == 'POST':
        for question in survey.questions.all():
            answer_text = request.POST.get(f'question_{question.id}')
            if answer_text:
                Answer.objects.create(
                    response=response,
                    question=question,
                    answer_text=answer_text
                )
        
        return redirect('polls:survey_complete', survey_id=survey_id)
    
    return render(request, 'polls/answer_form.html', {
        'survey': survey,
        'response': response
    })

def survey_complete(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, 'polls/complete.html', {'survey': survey})

def question_detail(request, survey_id, question_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    question = get_object_or_404(Question, pk=question_id, survey=survey)
    return render(request, 'polls/question_detail.html', {'survey': survey, 'question': question})

def vote(request, survey_id, question_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    question = get_object_or_404(Question, pk=question_id, survey=survey)
    
    if request.method == 'POST':
        answer_text = request.POST.get('answer')
        if not answer_text:
            return render(request, 'polls/question_detail.html', {
                'survey': survey,
                'question': question,
                'error_message': "답변을 입력해주세요.",
            })
        
        Answer.objects.create(
            response=Response.objects.create(survey=survey, nickname="Anonymous"),
            question=question,
            answer_text=answer_text
        )
        return HttpResponseRedirect(reverse('polls:question_detail', args=(survey.id, question.id,)))
    
    return render(request, 'polls/question_detail.html', {
        'survey': survey,
        'question': question
    })