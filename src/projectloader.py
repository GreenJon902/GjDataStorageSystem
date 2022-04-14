import json
import threading
from typing import Callable

from betterLogger import ClassWithLogger
from kivy.clock import Clock


projects_file_path = "P:/map.json"


class Project:
    id: int
    name: str
    type: str
    status: list[str]

    tags: dict[str: any]

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id")
        self.name = kwargs.pop("name")
        self.type = kwargs.pop("type")
        self.status = kwargs.pop("status", [])

        self.tags = kwargs.pop("tags", {})

        if len(kwargs) != 0:
            raise TypeError("Too many arguments supplied")

    def __repr__(self):
        return f"Project(id={self.id}, name={self.name}, type={self.type}, status={self.status}, tags={self.tags})"


class ProjectList:
    _projects: dict[Project]

    def __init__(self, from_string=None):
        if from_string:
            self._projects = eval(from_string)

    def __repr__(self):
        return repr(self._projects)

    def __iter__(self):
        return iter(self._projects.values())


class ProjectLoader(ClassWithLogger):
    _projects: ProjectList = None

    def get_project(self, id: int, callback: Callable[[Project], None]):
        pass

    def get_all_projects(self, callback: Callable[[ProjectList], None]):
        self.log_debug("Getting all projects")
        if self._projects:
            callback(self._projects)
        else:
            async_run(self._load_projects, lambda _: callback(self._projects))


    def _load_projects(self):
        self.log_info("Loading projects file")
        self.log_debug(f"Loading {projects_file_path}")
        projects = open(projects_file_path, "r").read()
        self._projects = ProjectList(from_string=projects)


def async_run(function, callback):
    def async_run_wrapper(_function, _callback):
        _function()
        Clock.schedule_once(_callback)
    threading.Thread(target=async_run_wrapper, args=(function, callback)).start()
