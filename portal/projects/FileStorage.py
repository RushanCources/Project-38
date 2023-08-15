import os
import pathlib
import re

from django.core.exceptions import SuspiciousFileOperation
from django.core.files.storage import FileSystemStorage
from django.core.files.utils import validate_file_name


# Увеличивает номер в скобках в самом конце файла или создаёт этот номер
def increase_file_name(file_root: str):
    if re.match(r'.+_\d+_$', file_root):
        number = int(file_root[file_root.rfind('_', 0, -1)+1:-1])
        return file_root[:file_root.rfind('_', 0, -1)+1]+str(number+1)+'_'
    return file_root + '_1_'


class MyStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        # Этот код я просто скопировал из исходника
        """
                Return a filename that's free on the target storage system and
                available for new content to be written to.
                """
        name = str(name).replace("\\", "/")
        dir_name, file_name = os.path.split(name)
        if ".." in pathlib.PurePath(dir_name).parts:
            raise SuspiciousFileOperation(
                "Detected path traversal attempt in '%s'" % dir_name
            )
        validate_file_name(file_name)
        file_root, file_ext = os.path.splitext(file_name)
        increase_file_root = file_root
        # If the filename already exists, generate an alternative filename
        # until it doesn't exist.
        # Truncate original name if required, so the new filename does not
        # exceed the max_length.
        while self.exists(name) or (max_length and len(name) > max_length):
            increase_file_root = increase_file_name(increase_file_root)
            # file_ext includes the dot.
            name = os.path.join(
                dir_name, increase_file_root+file_ext  # здесь поставлено увеличение значения числа в скобочках вместо добавления нескольких случайных символов
            )
            if max_length is None:
                continue
            # Truncate file_root if max_length exceeded.
            truncation = len(name) - max_length
            if truncation > 0:
                file_root = file_root[:-truncation]
                # Entire file_root was truncated in attempt to find an
                # available filename.
                if not file_root:
                    raise SuspiciousFileOperation(
                        'Storage can not find an available filename for "%s". '
                        "Please make sure that the corresponding file field "
                        'allows sufficient "max_length".' % name
                    )
                increase_file_root = increase_file_name(file_root)
                name = os.path.join(
                    dir_name, increase_file_root + file_ext  # здесь поставлено увеличение значения числа в скобочках вместо добавления нескольких случайных символов
                )
        return name
