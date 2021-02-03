from django import forms 
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('asker','date_asked')

class AnswerForm(forms.ModelForm):
    class Meta:  
        model = Answer 
        exclude = ('question','author','date_answered')
