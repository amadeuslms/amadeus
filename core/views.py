# Create your views here.

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings

from forms import UserForm
from models import User


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            msg = u'Ola, %s, \n Seja bem vindo(a) ao Amadeus. Este e um email de confirmacao de cadastro. Confira todos os dados: \n\n Nome: %s \n Email: %s \n Data de Nascimento: %s' %  (user.name, user.name, user.email, user.birthday)

            send_mail(subject=u'Cadastro Realizado com Sucesso!',
                            message=msg,
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[user.email])
            return HttpResponseRedirect(reverse('core:success', args=[user.pk]))
    else:
        form = UserForm()

    context = RequestContext(request, {'form': form})
    return render_to_response('users/new.html', context)

def success(request, pk):
    usert = get_object_or_404(User, pk=pk)
    context = RequestContext(request, {'usert': usert}) #dentro das chaves esta havendo a declaracao de um bean e o RequestContext esta adicionando esse bean ao contexto.
    return render_to_response('users/success.html', context)