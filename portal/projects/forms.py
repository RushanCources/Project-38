from django import forms


class FileForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='Выберите файлы',
    )