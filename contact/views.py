from django.shortcuts import render
from django.contrib import messages
from .forms import FeedbackForm


def contact_page(request):
    if request.method == "POST":
        feedback_form = FeedbackForm(data=request.POST)

        if feedback_form.is_valid():
            feedback.save()

    feedback_form = FeedbackForm()

    return render(
        request,
        "contact/contact_page.html",
        {
            "feedback_form": feedback_form
        },
    )