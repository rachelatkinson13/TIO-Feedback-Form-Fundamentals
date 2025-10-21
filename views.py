from django.http import HttpResponseRedirect
from django.shortcuts import render
from  django.views import View
from . forms import FeedbackForm
from . models import Feedback

# Create your views here.
class FeedbackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, "formactivity/form.html", {
        "form": form
    })
        
    def post(self, request):
        form = FeedbackForm(request.POST)     #        form = ReviewForm(request.POST, instance=existing_data)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "formactivity/form.html", {
        "form": form
    })
    
def thank_you(request):
    return render(request, "formactivity/thank_you.html")