from abc import ABC, abstractmethod


class Page(ABC):

    @abstractmethod
    def serve(self):
        pass
