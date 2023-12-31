from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Photo

@login_required
def photo_list(request):
    user_photos = Photo.objects.filter(author=request.user)
    return render(request, 'photo/list.html', {'user_photos': user_photos})
class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'