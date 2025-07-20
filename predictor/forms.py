from django import forms

class StudentInputForm(forms.Form):
    GENDER_CHOICES = [('male', 'male'), ('female', 'female')]
    TESTPREP_CHOICES = [('completed', 'completed'), ('none', 'none')]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    math_score = forms.FloatField(label="Math Score")
    reading_score = forms.FloatField(label="Reading Score")
    writing_score = forms.FloatField(label="Writing Score")
    test_prep = forms.ChoiceField(choices=TESTPREP_CHOICES, label="Test Preparation")
    avg_score = forms.FloatField(label="Average Score")
