from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=200, verbose_name='설문조사 제목')
    description = models.TextField(verbose_name='설문조사 설명', blank=True)
    pub_date = models.DateTimeField('게시일')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '설문조사'
        verbose_name_plural = '설문조사'

class Question(models.Model):
    QUESTION_TYPES = (
        ('text', '단답형'),
        ('textarea', '주관식'),
        ('choice', '객관식'),
    )
    
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='설문조사', related_name='questions')
    question_text = models.CharField(max_length=200, verbose_name='질문')
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='text', verbose_name='질문 유형')
    order = models.IntegerField(verbose_name='질문 순서', default=0)
    choice_options = models.TextField(verbose_name='객관식 선택지', blank=True, help_text='객관식 선택지를 줄바꿈으로 구분하여 입력하세요. 정답은 앞에 *를 붙여주세요.')
    
    def __str__(self):
        return self.question_text
    
    def get_choices(self):
        if not self.choice_options:
            return []
        return [{'text': line.strip('* '), 'is_correct': line.strip().startswith('*')} 
                for line in self.choice_options.split('\n') if line.strip()]
    
    class Meta:
        verbose_name = '질문'
        verbose_name_plural = '질문'
        ordering = ['order']

class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='설문조사', related_name='responses')
    nickname = models.CharField(max_length=50, verbose_name='닉네임')
    submitted_at = models.DateTimeField('제출일', auto_now_add=True)
    
    def __str__(self):
        return f"{self.nickname}의 응답 - {self.survey.title}"
    
    class Meta:
        verbose_name = '응답'
        verbose_name_plural = '응답'

class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, verbose_name='응답', related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='질문', related_name='answers')
    answer_text = models.TextField(verbose_name='답변')
    is_correct = models.BooleanField(default=False, verbose_name='정답 여부')
    
    def __str__(self):
        return f"{self.response.nickname}의 답변 - {self.question.question_text}"
    
    def save(self, *args, **kwargs):
        if self.question.question_type == 'choice':
            choices = self.question.get_choices()
            for choice in choices:
                if choice['text'] == self.answer_text:
                    self.is_correct = choice['is_correct']
                    break
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = '답변'
        verbose_name_plural = '답변'