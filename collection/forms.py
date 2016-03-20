from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField()
	contact_email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Your name:"
		self.fields['contact_email'].label = "Your email:"
		self.fields['content'].label = "What do you want to say?"