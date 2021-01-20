from django import forms


class MainLoadForm(forms.Form):
    url = forms.CharField(max_length=100, required=False, label='Ссылка')
    image = forms.ImageField(required=False, label='Файл')
    flag1 = False
    flag2 = False

    def clean_url(self):
        if data := self.cleaned_data.get('url'):
            self.flag1 = True
            return data

    def clean_image(self):
        if data := self.cleaned_data.get('image'):
            self.flag2 = True

        if not self.flag1 and not self.flag2 or self.flag1 and self.flag2:
            raise forms.ValidationError(
                'Ошибка: оба поля не могут быть заполнены или быть пустыми.')
        return data


class ChangeResolutionForm(forms.Form):
    width = forms.IntegerField(required=False, label='Ширина')
    height = forms.IntegerField(required=False, label='Высота')
