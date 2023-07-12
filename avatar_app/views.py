from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Character

class CharacterListView(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'characters.html'
    context_object_name = 'characters'

class CharacterDetailView(LoginRequiredMixin, DetailView):
    model = Character
    template_name = 'character_detail.html'

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    fields = ['name', 'description', 'image', 'nation']
    template_name = 'character_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    model = Character
    fields = ['name', 'description', 'image', 'nation']
    template_name = 'character_form.html'

class CharacterDeleteView(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = '/'
    template_name = 'character_confirm_delete.html'
