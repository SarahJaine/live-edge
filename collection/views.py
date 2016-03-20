from django.contrib import messages
from django.template.loader import get_template 
from django.core.mail import EmailMessage
from django.template import Context

from django.shortcuts import render, redirect
from collection.forms import ContactForm


# Create your views here.
def index(request):
	return render(request, 'index.html')

def contact(request): 
	form_class = ContactForm

	## Email logic
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			form_content = form.cleaned_data['content']
			
			## Email the profile with the contact info 
			template = get_template('contact_template.txt')

			context = Context({ 
				'contact_name': contact_name, 
				'contact_email': contact_email,
				'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage(
				'New contact form submission', 
				content,
				'Your website', 
				['youremail@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			messages.success(request, "Success! Message sent.")
			return redirect('contact')
		else:
			# for key, value in form.errors:
			# 	messages.error(request, form.errors[value])
			messages.error(request, "Error! Please check the inputs.")
			return redirect('contact')

	return render(request, 'contact.html', { 
		'form': form_class,

	})
