from src.projectloader import ProjectLoader, ProjectList
from src.widgets.pages.page import Page


class ProjectSearchPage(Page):
    projectLoader: ProjectLoader

    def __init__(self, **kwargs):
        Page.__init__(self, **kwargs)
        self.projectLoader = ProjectLoader()
        self.projectLoader.get_all_projects(self.update_content)

    def update_content(self, content: ProjectList):
        pass
