from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import models, forms
from django.http import HttpResponse
from django.views import generic

class FilmsListView(generic.ListView):
    template_name = 'film_list.html'
    queryset = models.Films.objects.all()

    def get_queryset(self):
        return models.Films.objects.all()


class FilmDetailView(generic.DetailView):
    template_name = "film_detail.html"

    def get_object(self, **kwargs):
        films_id = self.kwargs.get("id")
        return get_object_or_404(models.Films, id=films_id)


class FilmsCreateView(generic.CreateView):
    template_name = "add_films.html"
    form_class = forms.FilmForm
    queryset = models.Films.objects.all()
    success_url = "/films/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(FilmsCreateView, self).form_valid(form=form)


# def add_film(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.FilmForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Film created')
#     else:
#         form = forms.FilmForm
#     return render(request, 'add_films.html', {'form': form})



class FilmsUpdateView(generic.UpdateView):
    template_name = "film_update.html"
    form_class = forms.FilmForm
    success_url = "/films/"

    def get_object(self, **kwargs):
        film_id = self.kwargs.get("id")
        return get_object_or_404(models.Films, id=film_id)

    def form_valid(self, form):
        return super(FilmsUpdateView, self).form_valid(form=form)


# def film_update(request, id):
#     film_object = get_object_or_404(models.Films, id=id)
#     if request.method == 'POST':
#         form = forms.FilmForm(instance=film_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Film update succesfully')
#             return redirect(reverse("films:films_all"))
#     else:
#         form = forms.FilmForm(instance=film_object)
#     return render(request, 'film_update.html', {'form': form, 'object': film_object})


class FilmsDeleteView(generic.DeleteView):
    template_name = "confirm_delete_film.html"
    success_url = '/films/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get("id")
        return get_object_or_404(models.Films, id=film_id)
# def film_delete(request, id):
#     film_object = get_object_or_404(models.Films, id=id)
#     film_object.delete()
#     return HttpResponse('Film Deleted')


class FilmComment(FilmDetailView):
    template_name = "film_detail.html"

    def get_object(self, **kwargs):
        comment = self.kwargs.get("comment")
        return get_object_or_404(models.Comment, comment=comment)
