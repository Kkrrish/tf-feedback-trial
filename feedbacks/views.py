from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
import csv
from .forms import FeedbackForm

response_sheet = csv.writer(open("Responses.csv", "a"))
print "********Response Sheet Ready********"
#response_sheet.writerow(["Name","Feedback"])


def feedback(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			#process
			print form.cleaned_data
			#sheet = csv.writer(open('Responses.csv','a'))
			response_sheet.writerow([str(form.cleaned_data['his_name']),str(form.cleaned_data['his_feedback'])])			
			#sheet.writerow("ek response aya")	
			print "****Recorded****"
			#deliver to end-point
			return render(request, 'feedbackTrial/thanksPage.html')			
	else:
		form = FeedbackForm()
		#pass
		#return render(request, 'feedbackTrial/feedbackForm.html', { 'foo': 'bar',})

	return render(request, 'feedbackTrial/feedbackForm.html', { 'form': form})
