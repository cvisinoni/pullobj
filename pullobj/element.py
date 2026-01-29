from .logger import log
from datetime import datetime
from pathlib import Path
from copy import deepcopy
import os


class Element:

    root: Path = None

    def __init__(self, key: str, path: str, last_update_date: datetime, **kwargs):
        self.key = key
        self.path = path
        self.last_update_date = last_update_date
        self.kwargs = kwargs

    @classmethod
    def from_dict(cls, data: dict):
        kwargs = deepcopy(data)
        key = kwargs.pop('key')
        path = kwargs.pop('path')
        last_update_date = kwargs.pop('last_update_date')
        if isinstance(last_update_date, str):
            last_update_date = datetime.fromisoformat(last_update_date)
        return cls(key, path, last_update_date, **kwargs)

    @property
    def file(self):
        return self.root / self.path

    def to_dict(self):
        result = dict(
            key=self.key,
            path=self.path,
            last_update_date=self.last_update_date.isoformat(),
        )
        for key, value in self.kwargs.items():
            result[key] = value
        return result

    def delete(self):
        if self.file.is_file():
            log.debug(f'deleting {self.file}')
            os.remove(self.file)

    def save(self, content: str | bytes):
        if isinstance(content, str):
            content = content.encode('utf-8')
        if isinstance(content, bytes):
            log.debug(f'saving {self.file}')
            self.file.parent.mkdir(parents=True, exist_ok=True)
            self.file.write_bytes(content)
        else:
            log.warning(f'content of {self.key} is not str or bytes ({type(content)})')
