from django.shortcuts import render, redirect
from .forms import StudentInputForm
from .predictor_utils import predict_student_performance

def predictor_view(request):
    result = None

    if request.method == "POST":
        form = StudentInputForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data["gender"]
            math_score = form.cleaned_data["math_score"]
            reading_score = form.cleaned_data["reading_score"]
            writing_score = form.cleaned_data["writing_score"]
            testprep = form.cleaned_data["test_prep"]
            avg_score = form.cleaned_data["avg_score"]

            # Call prediction function
            result = predict_student_performance(gender, math_score, reading_score, writing_score, testprep, avg_score)

    else:
        form = StudentInputForm()

    return render(request, "forms.html", {"form": form, "result": result})

