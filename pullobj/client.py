from .element import Element
from .utils import load_json, save_json
from .logger import log
from pathlib import Path


class Client:

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.objectsinfo = dict()
        self.element_class = type[Element](
            Element.__name__, (Element,), dict(root=self.root)
        )

    @property
    def objectsinfo_file(self):
        return self.root / '.objectsinfo.json'

    def load_objectsinfo(self):
        if self.objectsinfo_file.exists():
            content = load_json(self.objectsinfo_file)
            for key, data in content.items():
                element = self.element_class.from_dict(data)
                self.objectsinfo[key] = element

    def save_objectsinfo(self):
        save_json(self.objectsinfo_file, {
            key: element.to_dict() for key, element in self.objectsinfo.items()
        })

    def retrieve_elements_dict(self):
        raise NotImplementedError('Not implemented')

    def retrieve_an_element_content(self, element: Element):
        raise NotImplementedError('Not implemented')

    def pull(self):
        log.debug(f'--- start pull elements for client {self.root} ---')
        # load old objectsinfo and retrieve new dict
        self.load_objectsinfo()
        elements_dict = self.retrieve_elements_dict()

        # delete elements that are not in the new dict
        for key, element in list(self.objectsinfo.items()):
            if key not in elements_dict:
                element.delete()
                self.objectsinfo.pop(key)

        # export elements that are in the new dict
        for key, value in elements_dict.items():
            new_element: Element = self.element_class.from_dict(value)
            if key in self.objectsinfo:
                old_element = self.objectsinfo[key]
                if old_element.last_update_date >= new_element.last_update_date and old_element.file.is_file():
                    continue
            content = self.retrieve_an_element_content(new_element)
            new_element.save(content)
            self.objectsinfo[key] = new_element

        # update file objectsinfo
        self.save_objectsinfo()
