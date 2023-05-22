from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Announcement


class AnnouncementForm(forms.Form):
    date_of_expiring = forms.DateField(label='', widget=forms.DateInput(attrs={'class': 'date', 'type': 'date'}), required=False)
    title = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'title', 'placeholder' : 'Заголовок объявления'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'body'}))
    is_pinned = forms.BooleanField(label='Закрепить', required=False)
    image_url = forms.FilePathField(label='Выбрать обложку', path='static/img/announcements/covers', required=False, widget=forms.TextInput(attrs={'class': 'imurl'}))
    files = forms.FileField(label='Прикрепить файлы', widget=forms.FileInput(attrs={'class':"files"}), required=False)
    file_id_to_delete = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'fitd'}), required=False)

    def clean_date_of_expiring(self):
        exdate = self.cleaned_data.get('date_of_expiring')
        if exdate is not None and datetime.now().date() > exdate:
            raise ValidationError('Неверная дата')
