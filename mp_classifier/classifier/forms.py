from django import forms

CATEGORY_CHOICE = (
    ('MC', 'Malaria Classification'),
    ('PC' ,'Pneumonia Classification')
)


class ClassifierForm(forms.Form):
    image = forms.ImageField(required=True)
    category = forms.ChoiceField(choices=CATEGORY_CHOICE)