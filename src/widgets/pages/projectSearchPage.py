from src.projectloader import ProjectLoader
from src.widgets.pages.page import Page


class ProjectSearchPage(Page):
    projectLoader: ProjectLoader

    def __init__(self, **kwargs):
        Page.__init__(self, **kwargs)
        self.projectLoader = ProjectLoader()
        self.projectLoader.get_all_projects(print)
