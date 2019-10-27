from abc import abstractmethod


class BaseService:

    @abstractmethod
    def start(self, login, password, data):
        pass
