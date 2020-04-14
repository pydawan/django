from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import UploadFileForm, UploadFilesForm
from .models import UploadFile


def index(request):
    files = UploadFile.objects.all()
    return render(
        request=request,
        template_name='upload/index.html',
        context={'files': files},
    )


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('upload:index'))
    else:
        form = UploadFileForm()
    return render(
        request=request,
        template_name='upload/file.html',
        context={'form': form},
    )


def upload_files(request):
    if request.method == 'POST':
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for file in files:
                instance = UploadFile(file=file)
                instance.save()
            return HttpResponseRedirect(reverse('upload:index'))
    else:
        form = UploadFilesForm()
    return render(
        request=request,
        template_name='upload/files.html',
        context={'form': form},
    )


def update_file(request, pk):
    file = get_object_or_404(UploadFile, pk=pk)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('upload:index'))
    else:
        form = UploadFileForm(instance=file)
    return render(
        request=request,
        template_name='upload/file.html',
        context={'form': form},
    )


def delete_file(request, pk):
    obj = UploadFile.objects.get(pk=pk)
    if request.method == "POST":
        obj.file.delete()
        obj.delete()
        return HttpResponseRedirect(reverse('upload:index'))
    else:
        return render(
            request=request,
            template_name='base/snippets/confirm-delete.html',
            context={'obj': obj},
        )
