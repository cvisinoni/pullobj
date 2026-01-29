from pullobj import Element, Client
from datetime import datetime
import logging


# Enable logging for monitoring the library log messages
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)16s - %(levelname)8s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.getLogger('pullobj').setLevel(logging.DEBUG)


# Optionally, you can extend the Element class and override it in the client constructor
class MyElement(Element):
    # ...
    pass


# Define custom Client
class MyClient(Client):

    def __init__(self, environment):
        super().__init__(f'output/myclient/{environment}')
        self.element_class = type[MyElement](
            MyElement.__name__, (MyElement,), dict(root=self.root)
        )


    def retrieve_elements_dict(self):
        """
        Return a dictionary with the required fields:
            - key: a unique ID for the element
            - path: a relative path to save the element file
            - last_update_date: a datetime representing the last time the element was updated
        """
        result = dict()
        for i in range(10):
            key = f'element{i}'
            path = ('even/' if i % 2 == 0 else 'odd/') + f'{i:0>2}.txt'
            result[key] = {
                'key': key,
                'path': path,
                'last_update_date': datetime(1955, 11, 5, 8, 0),
                'other': f'value for {i} element'
            }
        return result

    def retrieve_an_element_content(self, element: Element):
        """
        Return the content of the element to save as str or bytes
        """
        return element.kwargs.get('other')


if __name__ == '__main__':

    myclient = MyClient('TEST')
    myclient.pull()

    myclient = MyClient('PROD')
    myclient.pull()
