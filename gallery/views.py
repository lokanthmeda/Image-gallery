from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from .models import Post, Image
from .forms import ImageForm, ImageFormSet
from django.db import transaction
from django.http.response import HttpResponse


class PostList(ListView):
    model = Post
    context_object_name = 'gallery'


class PostCreate(CreateView):
    model = Post
    fields = ['category', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_formset'] = ImageFormSet()
        return context

    def form_valid(self, form):
        image_formset = ImageFormSet(self.request.POST, self.request.FILES)
        with transaction.atomic():
            self.object = form.save()

            if image_formset.is_valid():
                image_formset.instance = self.object
                image_formset.save()
        return super().form_valid(form)


class PostDetail(DetailView):
    model = Post




def PostDelete(request,pk):
    po = Post.objects.filter(id = pk)
    po.delete()
    dat = Post.objects.all()
    return render(request,'gallery/post_confirm_delete.html',{'dat':dat})



def search_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)

        fdata = Post.objects.filter(category=search_query)

        if len(fdata) != 0:

            return render(request, 'gallery/post-search.html', {'data': fdata})
        else:
            return HttpResponse('Not Found')

