from django import forms

class registrationForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=25)
    lastName = forms.CharField(label='Last name', max_length=25)
    email = forms.CharField(label="email", max_length=50)
    password = forms.CharField(label="password", max_length=255)
    # def __init__(self, *args, **kwargs):
    #     super(registrationForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'