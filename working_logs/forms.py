from django import forms
from .models import Project, Opinion
from django.forms import SelectDateWidget
from datetime import datetime

y = datetime.now().strftime('%Y')
Y = int(y)
YEARS = [(Y+i) for i in range(-5, 5)]
MONTHS = {
    1:1, 2:2, 3:3, 4:4,
    5:5, 6:6, 7:7, 8:8,
    9:9, 10:10, 11:11, 12:12
}
d = [i for i in range(1, 32)]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['text', 'date_added']
        labels = {'text': '项目名称  ', 'date_added': '添加时间'}
        widgets = {'date_added': SelectDateWidget(years=YEARS, months=MONTHS)}

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['text', 'date_added']
        labels = {'text': '', 'date_added': '添加时间'}
        widgets = {'date_added': SelectDateWidget(years=YEARS, months=MONTHS),
         'text': forms.Textarea(attrs={'cols': 80})
        }

