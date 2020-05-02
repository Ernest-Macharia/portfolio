from django.shortcuts import render
from django.http import HttpResponse
import json
from . models import Contact

#home view
def index(request):
	#check if the method is post and request type
	if request.method == 'POST' and request.is_ajax():
		#check for name field
		if request.POST['name'] == "":
			username = "Margret Wambui" #default name
		else:
			username = request.POST['name']

		#check for select field
		if request.POST['gender'] == "Select":
			gender = "f"
		else:
			gender = request.POST['gender']

		#return name and gender to success in ajax call top update content
		return HttpResponse(json.dumps({'name':username, 'gender':gender}))
	else:
		return render(request, 'myprofile/home.html')


#portfolio view 
def portfolio(request):
	return render(request, 'myprofile/projects.html')

#contact view
def contact(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		form = Contact(email=email, subject=subject, message=message)
		#saving the data from the form to the database
		form.save()
		return render(request, 'myprofile/contact.html')
	else:
		return render(request, 'myprofile/contact.html')

