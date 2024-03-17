from django import forms 
from django.contrib.auth.models import User
import re
from customer.models import CustomerModel

class RegisterForm(forms.Form):
    # username = forms.CharField(label="Tai khoan", max_length=50, required=True)
    username = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Verification", required=True, widget=forms.PasswordInput)
    full_name = forms.CharField(label="Full Name")
    phone_number = forms.CharField(label="Phone Number")
    address = forms.CharField(label="Address")

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 and password1 == password2:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        # if not re.search(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$', username):
        #     raise forms.ValidationError("Email khong hop le")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Email da ton tai trong he thong")

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password1"],
            # email=self.cleaned_data["email"],
            # last_name=self.cleaned_data["last_name"],
            # first_name=self.cleaned_data["first_name"],
            # is_staff=True,
        )
        customer = CustomerModel(
            user = user,
            full_name=self.cleaned_data["full_name"],
            phone_number=self.cleaned_data["phone_number"],
            address=self.cleaned_data["address"],
        )
        customer.save()