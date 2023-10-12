from django import forms
from Trobinoscoop.models import Person,Student,Employee
class LoginForm(forms.Form):
    email=forms.EmailField(label='Courriel')
    password= forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data=super(LoginForm,self).clean()
        email=cleaned_data.get("email")
        password=cleaned_data.get("password")
        if email and password:
            result=Person.objects.filter(password=password, email=email)
            if len(result) != 1:
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné(e)")
        return cleaned_data
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude = ("friends",)
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ("friends",)

class AddFriendForm(forms.Form):
    email=forms.EmailField(label="Courriel:")
    def clean(self):
        cleaned_data= super(AddFriendForm, self).clean()
        email= cleaned_data.get("email")
        if email:
            result=Person.objects.filter(email=email)
            if len(result) != 1:
                raise forms.ValidationError("Adresse de courriel erronée.")
            return cleaned_data