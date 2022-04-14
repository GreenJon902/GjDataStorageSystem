from typing import Callable


class Project:
    id: int
    name: int


class Loader:
    def get_project(self, id: int, callback: Callable[[Project], None]):
        pass

    def get_all_project(self, callback: Callable[[list[Project]], None]):
        pass
