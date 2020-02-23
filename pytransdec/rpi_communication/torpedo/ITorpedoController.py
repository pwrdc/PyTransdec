import abc


class ITorpedoController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_torpedo_data(self):
        pass

    @abc.abstractmethod
    def log(self, msg, logtype):
    	pass
