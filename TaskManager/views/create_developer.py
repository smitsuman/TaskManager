from TaskManager.models import Supervisor, Developer
from django.shortcuts import render
from django import forms
# This line imports the Django forms package
class Form_inscription(forms.Form):
# This line creates the form with four fields. It is an object that
#inherits from forms.Form. It contains attributes that define the form
#fields.
    error_name = {'required': 'You must type a name !','invalid': 'Wrong format.'}
    name = forms.CharField(label="Name", max_length=30, error_messages=error_name)
    login = forms.CharField(label="Login", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all())
    def clean(self):
        cleaned_data = super (Form_inscription, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data
# View for create_developer
def page(request):
    if request.POST:
        form = Form_inscription(request.POST)
# If the form has been posted, we create the variable that will
#contain our form filled with data sent by POST form.
        if form.is_valid():
# This line checks that the data sent by the user is consistent
#with the field that has been defined in the form.
            name = form.cleaned_data['name']
# This line is used to retrieve the value sent by the client. The
#collected data is filtered by the clean() method that we will see
#later. This way to recover data provides secure data.
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']
# In this line, the supervisor variable is of the Supervisor
#type, that is to say that the returned data by the cleaned_data
#dictionary will directly be a model.
            new_developer = Developer(name=name, login=login, password=password, email="", supervisor=supervisor)
            new_developer.save()
            return HttpResponse("Developer added")
        else:
            return render(request, 'en/public/create_developer.html', {'form' : form})
# To send forms to the template, just send it like any other
#variable. We send it in case the form is not valid in order to display
#user errors:
    else:
        form = Form_inscription(initial={'name': 'new', 'supervisor':Supervisor.objects.all()[:1].get().id})
# In this case, the user does not yet display the form, it
#instantiates with no data inside.
        return render(request, 'en/public/create_developer.html', {'form': form})
