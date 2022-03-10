from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaultfilters import first
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from helloworld.models import Funcionario


class ListaFuncionarios(ListView):
    template_name = 'templates/funcionarios.html'
    model = Funcionario
    context_object_name = 'funcionarios'


class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self):
        funcionario = None

        # Os compos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            # Busca o funcionario apartir do id
            funcionario = Funcionario.objects.filter(id=id).first()

        elif slug is not None:
            # Pega o compo slug do Model
            campo_slug = self.get_slug_field()
            # Busca o funcionario apartir do slug
            funcionario = Funcionario.objects.filter(**{campo_slug: slug}).first()

        # Retorna o objeto encontrado
        return funcionario


class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    sucess_url = reverse_lazy(
        "website:lista_funcionarios"
    )


class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )


def cria_funcionario(request, pk):
    # Veficando se o método POST ...
    if request.mehtod == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.sabe()
            return HttpResponseRedirect(reverse('lista_funcionarios'))

        # Qualquer outro método: GET, OPTION, DELETE, etc...
        else:
            return render(request, "templates/from.html", {'form': form})
