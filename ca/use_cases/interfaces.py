from abc import ABCMeta, abstractmethod


class IUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
