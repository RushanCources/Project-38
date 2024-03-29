from dataclasses import dataclass
from typing import Any

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.request import HttpRequest
from django.contrib import messages

from management.models import User
from projects.models import Project, File
from subjects.models import Subject


def check_what_user_not_have_access(request: HttpRequest, project: Project):  # True если пользаватель не имеет прав для просмотра проекта, False, если имеет
    return request.user.id != project.teacher.id and request.user.id != project.student.id and request.user.role != 'Администратор'


# эта функция возвращает страницу со всеми вашими проектами или конкретный проект
def index(request: HttpRequest):
    project_id = request.GET.get("id", None)
    # здесь идёт исполнение кода и возвращается страница общих проектов, т.к. не указан конкретный проект
    if not request.user.is_authenticated:
        return render(request, 'base.html')
    
    if project_id is None:
        if request.user.role == 'Ученик':
            projects = Project.objects.filter(student=request.user)
        elif request.user.role == 'Учитель':
            projects = Project.objects.filter(teacher=request.user)
        elif request.user.role == 'Администратор':
            projects = Project.objects.all()
        else:
            projects = []

        # это класс для более удобного доступа к данным в шаблоне
        class ProjectPack(Project):
            files: list[File] = []

        # упаковка проектов и файлов в один массив состоящий из объектов класса ProjectPack
        
        context_projects = []

        for project in projects:
            files = list(File.objects.filter(project=project, version=1))
            variables = vars(project)
            values = {key : val for key, val in zip(variables.keys(), variables.values()) if key != '_state'}
            pp = ProjectPack(**values)
            pp.files = files
            context_projects.append(pp)

        return render(request, "projects/index.html", context={'projects': context_projects,
                                                               'has_projects': len(context_projects) > 0})
    # здесь идёт выполнение кода, кода был запрошен доступ к определённому проекту
    try:
        project = Project.objects.get(id=project_id)
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        abstract_file = File.objects.filter(project=project, version=1, _tag='Реферат').first()
        presentation_file = File.objects.filter(project=project, version=1, _tag='Презентация').first()
        annotation_file = File.objects.filter(project=project, version=1, _tag='Аннотация').first()
        other_files = File.objects.filter(project=project, version=1, _tag='Другое')
        full_teacher_name = project.teacher.last_name + ' ' + project.teacher.first_name + ' ' + project.teacher.middle_name
        full_student_name = project.student.last_name + ' ' + project.student.first_name + ' ' + project.student.middle_name
        context = {"name": project.name,
                   "teacher": full_teacher_name,
                   "student": full_student_name,
                   "avaurl_of_teacher": project.teacher.avatar.url,
                   "avaurl_of_student": project.student.avatar.url,
                   "status": project.get_status(),
                   "subjects" : project.get_subjects(),
                   "description": project.description,
                   "project_level": project.get_level(),
                   "project_type": project.get_type(),
                   'problem': project.problem,
                   "relevance": project.relevance,
                   "target": project.target,
                   "tasks": project.tasks,
                   "expected_results": project.expected_results,
                   "project_id": project_id,
                   'is_opened': request.user.is_view_window,
                   'abstract': abstract_file,
                   'old_abstracts': abstract_file.get_prevent_files() if abstract_file is not None else [],
                   'presentation': presentation_file,
                   'old_presentation': presentation_file.get_prevent_files() if presentation_file is not None else [],
                   'annotation': annotation_file,
                   'old_annotation': annotation_file.get_prevent_files() if annotation_file is not None else [],
                   'other_files': other_files,
                   'old_other_files': [other_file.get_prevent_files() for other_file in other_files],
                   'all_subjects_names': [subject.name for subject in Subject.objects.all()]
                   }

        return render(request, "projects/project_page.html", context=context)
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as error:
        print(error)
        return render(request, "FatalError.html")


# отправка страницы с формой для подачи заявки на проект
def send_create_form(request: HttpRequest, context_data={}):
    print(context_data)
    if request.user.is_authenticated:
        if request.user.role == "Ученик":
            teachers = User.objects.filter(role="Учитель", is_other_teacher=False)
            teacher_arr = []
            for teacher in teachers:
                teacher_arr.append([teacher.full_Name, teacher.id])
            data = {"teachers": teacher_arr,
                    "subjects_names": [subject.name for subject in Subject.objects.all()]}
            data.update(context_data)
            return render(request, "projects/create.html", data)
    return render(request, "NotEnoughPermissions.html")


# этот декоратор автоматически проверяет POST запрос на его метод, на наличие прав у пользователя и на наличие входящих данных
def check_post_request(*need_values):
    def decorator(func):
        def wrapper(request: HttpRequest):
            if request.method != 'POST':
                return redirect(reverse("projects"))
            if not request.user.is_authenticated:
                messages.error(request, 'У вас нет прав для совершения этого действия')
                return render(request, "")

            for value in need_values:
                request_value = request.POST.get(value, '')
                if request_value == '':
                    messages.error(request, 'Неверно введённые данные')
                    return render(request, request.get_full_path())
            return func(request)
        return wrapper
    return decorator


# эта функция обрабатывает запрос на заявку проекта
@check_post_request('name', "subject")
def create(request: HttpRequest):
    teacher_id = request.POST.get("teacher", -1)
    subject = request.POST.get("subject")
    name = request.POST.get("name")
    is_another_teacher = request.POST.get('teacher-checkbox')
    description = request.POST.get('description', '')

    try:

        if is_another_teacher == 'on':  # если учитель не из лицея
            another_teacher = request.POST.get("new-teacher", -1)
            if another_teacher == -1:
                messages.error(request, 'Неверно введённые данные')
                return send_create_form(request, context_data={'name': name, 'description': description})
            last_user = User.objects.last()
            if last_user is None:
                new_id = 1
            else:
                new_id = last_user.pk + 1
            teacher: User = User.objects.create_user(username=new_id, first_name=another_teacher.split()[1],
                                                     last_name=another_teacher.split()[0], middle_name=another_teacher.split()[2],
                                                     role='Учитель', id=new_id)
            teacher.set_password(User.objects.make_random_password(30))
            teacher.is_other_teacher = True
            teacher.save()
        else:
            if teacher_id == -1:
                messages.error(request, 'Неверно введённые данные')
                print({'name': name, 'description': description})
                return send_create_form(request, context_data={'name': name, 'description': description})
            teacher = User.objects.get(id=teacher_id)

        if teacher.role != "Учитель":
            return send_create_form(request, context_data={'name': name, 'description': description})
        project = Project.objects.create(name=name, teacher=teacher, student=request.user)
        if description != -1:
            project.description = description
        project.set_subject(subject)
        project.set_status("send request")
        project.save()
        files = request.FILES.getlist('files')
        for file in files:
            file_object = File.objects.create(project=project, file=file, version=1, _tag="Другое")
            file_object.save()
        return render(request, "projects/success.html")
    except User.DoesNotExist:  # если не удалось получить пользователя из бд
        return render(request, "WrongData.html")
    except BaseException as e:  # если возникла непредвиденная ошибка
        print(e)
        return render(request, "FatalError.html")


# в этой функции обрабатывается запрос о изменении данных проекта(имя, описанин
@check_post_request('project')
def correct_project(request: HttpRequest):
    project_id = request.POST.get("project")
    try:
        project = Project.objects.get(id=project_id)
        if check_what_user_not_have_access(request, project):  # провека на наличие прав у пользователья на изменение проекта
            return render(request, "NotEnoughPermissions.html")
        name = request.POST.get("name", -1)
        description = request.POST.get("description", -1)
        project_level = request.POST.get('project-level', -1)
        problem = request.POST.get('problem', -1)
        relevance = request.POST.get('relevance', -1)
        target = request.POST.get('target', -1)
        tasks = request.POST.get('tasks', -1)
        expected_results = request.POST.get('expected-results', -1)
        project_type = request.POST.get('project-type', -1)
        print(project_type)
        if name != -1:
            project.name = name
        if description != -1:
            project.description = description
        if project_level != -1:
            project.set_level(project_level)
        if problem != -1:
            project.problem = problem
        if relevance != -1:
            project.relevance = relevance
        if target != -1:
            project.target = target
        if tasks != -1:
            project.tasks = tasks
        if expected_results != -1:
            project.expected_results = expected_results
        if project_type != -1:
            project.set_type(project_type)
        project.save()
        request.user.is_view_window = True
        request.user.save()
        abstract_file = request.FILES.get('abstract', -1)
        presentation_file = request.FILES.get('presentation', -1)
        annotation_file = request.FILES.get('annotation', -1)
        if abstract_file != -1:
            file = File.objects.filter(project=project, version=1, _tag='Реферат').first()
            if  file is None:
                file = File.objects.create(project=project, file=abstract_file, version=1)
                file.set_tag('Реферат')
                file.save()
            else:
                file.update_file(abstract_file)
        if presentation_file != -1:
            file = File.objects.filter(project=project, version=1, _tag='Презентация').first()
            if  file is None:
                file = File.objects.create(project=project, file=presentation_file, version=1)
                file.set_tag('Презентация')
                file.save()
            else:
                file.update_file(presentation_file)
        if annotation_file != -1:
            file = File.objects.filter(project=project, version=1, _tag='Аннотация').first()
            if  file is None:
                file = File.objects.create(project=project, file=annotation_file, version=1)
                file.set_tag('Аннотация')
                file.save()
            else:
                file.update_file(annotation_file)
        return redirect(f"{reverse('projects')}?id={project_id}")
    except Project.DoesNotExist:  # если не удалось получить проект из бд
        return render(request, "WrongData.html")
    except BaseException as error:  # если возникла непредвиденная ошибка
        print(error)
        return render(request, "FatalError.html")


# обновление файла (замена предыдущего файла на новую его версию)
@check_post_request('file_id')
def update_file(request: HttpRequest):
    file_id = request.POST.get('file_id')
    file = request.FILES.get('file')
    try:
        file_object: File = File.objects.get(id=file_id)
        project = file_object.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file_object.update_file(file)
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:  # если не удалось получить фойл из бд
        return render(request, "WrongData.html")
    except Project.DoesNotExist:  # если не удалось получить проект из бд
        return render(request, "WrongData.html")
    except BaseException:  # если возникла непредвиденная ошибка
        return render(request, "FatalError.html")


# удаление файла(новейшая версия файла (1 - самая новая версия, 2 - версия по-старше и т.д) заменяется на -1,
# сам файл остаётся лежать на сервере, предыдущие версии файла не удаляются
@check_post_request('file_id')
def delete_file(request: HttpRequest):
    file_id = request.POST.get('file_id')
    try:
        file = File.objects.get(id=file_id)
        project = file.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file.move_to_trash()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:  # если не удалось получить фойл из бд
        return render(request, "WrongData.html")
    except BaseException:  # если возникла непредвиденная ошибка
        return render(request, "FatalError.html")


# загрузка файл на компьютр пользователя
def download_file(request: HttpRequest):
    file_id = request.GET.get('file_id', '')
    if file_id is None:
        return render(request, "WrongData.html")
    try:
        file_object = File.objects.get(id=file_id)
        if check_what_user_not_have_access(request, file_object.project):
            return render(request, "NotEnoughPermissions.html")
        filepath = file_object.file.path
        return FileResponse(open(filepath, 'rb'), as_attachment=True)
    except File.DoesNotExist:  # если не удалось получить фойл из бд
        return render(request, "WrongData.html")
    except BaseException:  # если возникла непредвиденная ошибка
        return render(request, "FatalError.html")


# загрузка файла на сервер
@check_post_request("project_id")
def upload_file(request: HttpRequest):
    project_id = request.POST.get("project_id")
    file = request.FILES.get("file")
    try:
        project = Project.objects.get(id=project_id)
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file_object = File.objects.create(project=project, file=file, version=1, _tag="Другое")
        file_object.save()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except Project.DoesNotExist:  # если не удалось получить проект из бд
        return render(request, "WrongData.html")
    except BaseException:  # если возникла непредвиденная ошибка
        return render(request, "FatalError.html")


# страница с удалёнными файлами
def get_trash(request: HttpRequest):
    project_id = request.GET.get('project_id')
    if project_id is None:
        return render(request, "WrongData.html")
    try:
        project = Project.objects.get(id=project_id)
        files = File.objects.filter(project=project, version=-1)
        names = [file.file.name.split('/')[-1] for file in files]
        files_and_names = zip(files, names)
        context = {"files": files_and_names}
        return render(request, "projects/trash.html", context=context)
    except Project.DoesNotExist:  # если не удалось получить проект из бд
        return render(request, "WrongData.html")
    except BaseException:  # если возникла непредвиденная ошибка
        return render(request, "FatalError.html")


# восстановление файла из корзины
@check_post_request('file_id')
def restore_file(request: HttpRequest):
    file_id = request.POST.get("file_id")
    try:
        file = File.objects.get(id=file_id)
        project = file.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file.restore()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException:
        return render(request, "FatalError.html")


# добавление комментария к фойлу
@check_post_request('comment', "file_id")
def set_comment(request: HttpRequest):
    comment = request.POST.get("comment")
    file_id = request.POST.get("file_id")
    try:
        file = File.objects.get(id=file_id)
        project = file.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file.comment = comment
        file.save()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException:
        return render(request, "FatalError.html")


# одобрение заявки на проект
@check_post_request('project_id')
def approve_project(request: HttpRequest):
    project_id = request.POST.get('project_id')
    try:
        project = Project.objects.get(id=project_id)
        if project.teacher.id == request.user.id or request.user.role == "Администратор":
            project.set_status('on work')
            return redirect(f"{reverse('projects')}?id={project.id}")
        return render(request, "NotEnoughPermissions.html")
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException:
        return render(request, "FatalError.html")


# закрытие проекта(проект доработан и сдан)
@check_post_request('project_id')
def close_project(request: HttpRequest):
    project_id = request.POST.get('project_id')
    try:
        project = Project.objects.get(id=project_id)
        if project.teacher.id == request.user.id or request.user.role == "Администратор":
            project.set_status('done')
            return redirect(f"{reverse('projects')}?id={project.id}")
        return render(request, "NotEnoughPermissions.html")
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException:
        return render(request, "FatalError.html")
