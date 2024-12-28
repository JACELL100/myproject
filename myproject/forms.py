from django import forms


class usersform(forms.Form):
    num1=forms.CharField(label="Value1",required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    num2=forms.CharField(label="Value2",widget=forms.TextInput(attrs={'class': "form-control"}))
    num3=forms.CharField(label="Value3",widget=forms.TextInput(attrs={'class': "form-control"}))
    email=forms.EmailField()