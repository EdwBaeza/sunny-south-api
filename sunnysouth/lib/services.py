
from abc import ABC, abstractclassmethod


class Service(ABC):

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    @abstractclassmethod
    def run(self):
        pass

    def before_run(self):
        pass

    def post_run(self):
        pass

    @classmethod
    def execute(cls, **kwargs):
        service = cls(**kwargs)
        service.before_run()
        response = service.run()
        service.post_run()

        return response

