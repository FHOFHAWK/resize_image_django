def save_uploaded_file(picture):
    filename, extension = picture.name.split('.')
    with open(f'media/images/{filename}.{extension}', 'wb+') as file:
        for chunk in picture.chunks():
            file.write(chunk)
    return f'images/{filename}.{extension}'
