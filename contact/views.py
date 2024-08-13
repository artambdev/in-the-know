from django.shortcuts import render
from .forms import FeedbackForm

def contact_page(request):
    feedback_form = FeedbackForm()

    return render(
        request,
        "contact/contact_page.html",
        {
            "feedback_form": feedback_form
        },
    )