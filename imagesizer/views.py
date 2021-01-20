from django.http import HttpResponseRedirect
from django.shortcuts import render

from imagesizer.forms import MainLoadForm, ChangeResolutionForm
from imagesizer.models import Image

import requests
from PIL import Image as im

from services import save_uploaded_file


def main(request):
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, template_name='main.html', context=context)


def load_image(request):
    if request.method == 'POST':
        form = MainLoadForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                if url := form.cleaned_data.get('url'):
                    img = requests.get(url).content
                    filename, extension = url.split('/')[-1].split('.')
                    with open(f'media/images/{filename}.{extension}', 'wb') as file:
                        file.write(img)
                    width, height = im.open(f'media/images/{filename}.{extension}').size
                    new_image = Image(title=filename, picture=f'images/{filename}.{extension}',
                                      width=width, height=height)
                    new_image.save()
                    return HttpResponseRedirect(f'/retrieve_image/{filename}')
            except requests.exceptions.InvalidSchema:
                return render(request, 'error.html')
            except ValueError:
                return render(request, 'error.html')

            if picture := form.cleaned_data.get('image'):
                path = save_uploaded_file(picture)
                filename = path.split('/')[-1].split('.')[0]
                width, height = im.open(f'media/{path}').size
                new_image = Image(title=filename, picture=path, width=width, height=height)
                new_image.save()
                return HttpResponseRedirect(f'/retrieve_image/{filename}')
    else:
        form = MainLoadForm()
    return render(request, 'form.html', {'form': form})


def retrieve_image(request, title):
    if request.method == 'POST':
        form = ChangeResolutionForm(request.POST)

        if form.is_valid():
            image = Image.objects.filter(title=title).first()
            if form.cleaned_data["height"] is not None:
                image.height = form.cleaned_data["height"]
            if form.cleaned_data["width"] is not None:
                image.width = form.cleaned_data["width"]
            image.save()
    try:
        image = Image.objects.filter(title=title).first()
        new_image = im.open(image.picture)
        new_image.thumbnail((image.width, image.height))
        title = f'new_{title}.png'
        picture_url = f'media/images/{title}'
        new_image.save(picture_url)

        picture_url = picture_url[6:]
        image = Image(title=title, picture=picture_url)
        form = ChangeResolutionForm()
        context = {
            "image": image,
            "form": form,
        }
        return render(request, template_name='image.html', context=context)
    except FileNotFoundError:
        return render(request, 'error.html')
