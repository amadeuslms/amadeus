from django import forms
from models import User
from core.validators import UsernameValidator
from core.validators import PasswordValidator

FORMACAO_PRINCIPAL_CHOICES = (('Ensino Superior Completo', 'Ensino Superior Completo'),
                                                        ('Ensino Superior em andamento', 'Ensino Superior em andamento'),
                                                        ('Pos-Graduacao Completa', 'Pos-Graduacao Completa'),
                                                        ('Pos-Graduacao em andamento', 'Pos-Graduacao em andamento'),)

SEX_CHOICES = (('m','Masculino'),
                          ('f','Feminino'),)

STATE_CHOICES = (('AC','AC'),
                              ('AL','AL'),
                              ('AM','AM'),
                              ('AP','AP'),
                              ('PA','PA'),
                              ('PB','PB'),
                              ('PE','PE'),
                              ('RN','RN'),)

ANO_FORMACAO_CHOICES = (('1980','1980'),
                                                ('1981','1981'),
                                                ('1982','1982'),
                                                ('1983','1983'),)

class UserForm(forms.ModelForm):
    username = forms.CharField(validators=[UsernameValidator], max_length=16)
    password = forms.CharField(validators=[PasswordValidator], widget=forms.PasswordInput(), max_length=16)
    confirmPassword = forms.CharField(validators=[PasswordValidator], widget=forms.PasswordInput(), max_length=16)
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES)
    birthday = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))
    state = forms.ChoiceField(widget=forms.Select, choices=STATE_CHOICES)
    formacaoPrincipal = forms.ChoiceField(widget=forms.Select, choices=FORMACAO_PRINCIPAL_CHOICES)
    anoFormacaoPrincipal = forms.ChoiceField(widget=forms.Select, choices=ANO_FORMACAO_CHOICES)

    class Meta:
        model = User

    def clean(self):
        super(UserForm, self).clean()

        if self.cleaned_data.get('password') != self.cleaned_data.get('confirmPassword'):
            raise forms.ValidationError('As senhas devem ser iguais.')
        return self.cleaned_data