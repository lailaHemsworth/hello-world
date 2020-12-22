from django import forms
class questionForm(forms.Form):
    text = forms.CharField(max_length= 50, widget = forms.TextInput(attrs= {'class' : 'col-md-11 col-sm-12  form-group',
                                                                             'placeholder' : 'Enter Question Here', 
                                                                             'aria-label' : 'question',
                                                                             'aria-describedby' : 'add-btn',
                                                                             }) )
