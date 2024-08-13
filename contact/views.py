from django.shortcuts import render
from django.contrib import messages
from .forms import FeedbackForm


def contact_page(request):
    if request.method == "POST":
        feedback_form = FeedbackForm(data=request.POST)

        if feedback_form.is_valid():
            feedback.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your feedback has been sent!'
            )
        else:
            messages.add_message(request, messages.ERROR, 'There was an error in sending your feedback')

    feedback_form = FeedbackForm()

    return render(
        request,
        "contact/contact_page.html",
        {
            "feedback_form": feedback_form
        },
    )