from django.shortcuts import render,redirect
from forms import FeedbackForm,FeedbackForm2
from models import Feedback, Category
# Create your views here.
def feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', locals())

def add(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()

            return redirect('/feedback/')


    else:
        feedback_form = FeedbackForm()
    return render(request, 'add.html', locals())
def update(request, id):
    feedback = Feedback.objects.get(pk=id)
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST,instance=feedback)
        if feedback_form.is_valid():
            feedback_form.save()
            return redirect('/feedback/')
    else:
        feedback_form = FeedbackForm(instance=feedback)
    return render(request, 'update.html', locals())

def add2(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm2(request.POST)
        if feedback_form.is_valid():
            name = feedback_form.cleaned_data['name']
            email = feedback_form.cleaned_data['email']
            message = feedback_form.cleaned_data['message']
            subject = feedback_form.cleaned_data['subject']

            Feedback.objects.create(name = name, email = email,
                                    message = message, subject_id = subject)

            return redirect('/feedback2/')
    else:
        choices = ((c.id, c.name) for c in Category.objects.all())
        feedback_form = FeedbackForm2()
        feedback_form.fields['subject'].choices = choices
    return render(request, 'add2.html', locals())
def feedback2(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback2.html', locals())

def update2(request, id):
    feedback = Feedback.objects.get(pk=id)
    if request.method == 'POST':
        feedback_form = FeedbackForm2(request.POST)
        if feedback_form.is_valid():
            feedback.name = feedback_form.cleaned_data['name']
            feedback.email = feedback_form.cleaned_data['email']
            feedback.message = feedback_form.cleaned_data['message']
            feedback.subject_id = feedback_form.cleaned_data['subject']

            feedback.save()

        return redirect('/feedback2/')
    else:
        feedback_form = FeedbackForm(initial={
            'name' : feedback.name,
            'email': feedback.email,
            'message': feedback.message,
            'subject': feedback.subject,
        })
    return render(request, 'update2.html', locals())