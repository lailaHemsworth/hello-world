from django.shortcuts import render
from django.shortcuts import redirect,HttpResponseRedirect
from .models import question
from .forms import questionForm
from django.views.decorators.http import require_POST
def create(request):
    question_list = question.objects.order_by('id')
    form  = questionForm()
    context = {'question_list' : question_list , 'form' : form}
  
    return render(request,'create.html', context)
@require_POST
def addQuestion(request):
    form = questionForm(request.POST)
    print(request.POST['text'])
    
    if form.is_valid():
        new_question = question(text = request.POST['text'])
        new_question.save()
    return redirect('create')
