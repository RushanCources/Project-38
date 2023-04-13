from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Announcement


class AnnouncementForm(forms.Form):
    title = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': '', 'placeholder' : 'Имя объявления'}))
    body = forms.CharField(label='', widget=forms.Textarea)
    is_pinned = forms.BooleanField(label='Закрепить', required=False)
    date_of_expiring = forms.DateField(label='Актуально до', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    image_url = forms.FilePathField(label='Выбрать обложку', path='static/img/announcements/covers', required=False)
    files = forms.FileField(label='Прикрепить файлы', widget=forms.FileInput(attrs={'multiple': True}), required=False)
    file_id_to_delete = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def clean_date_of_expiring(self):
        exdate = self.cleaned_data.get('date_of_expiring')
        if exdate is not None and datetime.now().date() > exdate:
            raise ValidationError('Неверная дата')
