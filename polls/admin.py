from django.contrib import admin
from django.forms import ModelForm, Textarea
from .models import Survey, Question, Response, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'question_type', 'order', 'choice_options']
        widgets = {
            'choice_options': Textarea(attrs={'rows': 5, 'placeholder': '선택지를 한 줄에 하나씩 입력하세요.\n정답인 선택지 앞에는 *를 붙여주세요.\n\n예시:\n*파이썬\n자바\nC++\n자바스크립트'})
        }

class QuestionInline(admin.TabularInline):
    model = Question
    form = QuestionForm
    extra = 3
    fields = ['question_text', 'question_type', 'order', 'choice_options']
    classes = ['collapse']
    
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.base_fields['choice_options'].widget.attrs['class'] = 'choice-options'
        return formset

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ['question', 'answer_text', 'is_correct']
    can_delete = False

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'survey', 'submitted_at')
    list_filter = ['survey', 'submitted_at']
    search_fields = ['nickname']
    inlines = [AnswerInline]
    readonly_fields = ['survey', 'nickname', 'submitted_at']

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]
    
    class Media:
        css = {
            'all': ['admin/css/forms.css']
        }
        js = ['admin/js/jquery.init.js', 'admin/js/inlines.js']

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)