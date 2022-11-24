
from mediaPage import Media
from va_api import VA_Action

class Action(Media,VA_Action):

    def __init__(self) -> None:
        super().__init__()