from abc import ABC, abstractmethod

class BaseController(ABC):
    @abstractmethod
    def execute_action(self, action):
        """Execute an action based on the recognized gesture."""
        pass