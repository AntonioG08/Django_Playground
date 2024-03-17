from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .forms import PageForm


# With this class we make sure that the current user is registered of from the staff
class StaffRequiredMixin(object):

    # This is the method to add decorators to a function for Django
    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
class PagesListView(ListView):
    # Page list
    model = Page
    template_name = 'pages/pages.html'


class PageDetailView(DetailView):
    # Page detal
    model = Page
    template_name = 'pages/page.html'


@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm

    """def get_success_url(self):
        return reverse('pages:pages')"""

    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

