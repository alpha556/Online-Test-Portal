from django.shortcuts import get_object_or_404
from .models import Exam, Report
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .form import UserForm
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@login_required(login_url='/exam/login/')
def index(request):
    exam_list = Exam.objects.all()
    return render(request, 'exam/index.html', {'exam_list': exam_list})


@login_required(login_url='/exam/login/')
def detail(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exam/detail.html', {'exam': exam})


def report(request):
    user = request.user
    if user.is_staff:
        result = Report.objects.all()
    else:
        result = Report.objects.filter(user=user)
    return render(request, 'exam/report.html', {'report': result, 'candidate': user})


""""
class user_login(View):
    form_class = UserLogin
    template_name = 'exam/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('exam:index')

            return render(request, self.template_name, {'form': form})
"""


@login_required(login_url='/exam/login/')
def submit(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    score = 0
    count = exam.question_set.count()

    for questions in exam.question_set.all():
        if request.POST.get(str(questions.pk)):
            response = request.POST.get(str(questions.pk))
            if str(questions.answer) == str(response):
                score += 1
    Report.objects.create(user=request.user, exam=exam, marks=score)
    return render(request, 'exam/submit.html', {'score': score, 'count': count})


class UserFormView(View):
    form_class = UserForm
    template_name = 'exam/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('exam:index')

            return render(request, self.template_name, {'form': form})
