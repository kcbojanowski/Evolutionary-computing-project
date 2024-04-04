from django import forms

class MyForm(forms.Form):
    text_field = forms.CharField(label='Text Field')
    email_field = forms.EmailField(label='Email Field')
    integer_field = forms.IntegerField(label='Integer Field')
    float_field = forms.FloatField(label='Float Field')
    boolean_field = forms.BooleanField(label='Boolean Field')
    date_field = forms.DateField(label='Date Field')
    choice_field = forms.ChoiceField(label='Choice Field', choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3')])
    multiple_choice_field = forms.MultipleChoiceField(label='Multiple Choice Field', choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3')])
