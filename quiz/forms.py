from django.forms import ModelForm
from .models import Results

class Score(ModelForm):
    class Meta():
        model = Results
        fields = ['username','quizname','score']


    