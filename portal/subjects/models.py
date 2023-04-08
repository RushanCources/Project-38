from django.db import models

class Theme(models.Model):
    themeNAME = models.CharField(max_length=100)  # Имя темы .. Хватит за глаза
    themeAUTHOR = models.CharField(max_length=30)  # Автор (тот, кто создал тему) .. Самаркандий Самаркандович влез
    themeSUPVISOR = models.CharField(max_length=30)  # Руководитель темы (преподаватель) .. Аналогично AUTHOR
    themeTYPE = models.CharField(max_length=10)  # Тип темы [Проект] или [НОУ], размер не важен, список выпадающий
    themeSUBJECT = models.CharField(max_length=20)  # Предметная область темы, опять же список выпадает
    themeSTATUS = models.CharField(max_length=20)  # Статус темы [Свободна], [Занята], [Прошлых лет]
    themeDESCRIPT = models.CharField(max_length=2000)  # Описание темы .. Доп. условия, и прочее, места хватить должно