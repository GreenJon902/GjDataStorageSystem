from kivy.uix.layout import Layout

from src.projectloader import ProjectLoader, ProjectList
from src.widgets.fields.projectField import ProjectField
from src.widgets.pages.page import Page


class ProjectSearchPage(Page):
    projectLoader: ProjectLoader

    def __init__(self, **kwargs):
        Page.__init__(self, **kwargs)
        self.projectLoader = ProjectLoader()

    def on_kv_post(self, base_widget):
        self.projectLoader.get_all_projects(self.update_content)

    def update_content(self, content: ProjectList):
        project_holder: Layout = self.ids.project_holder
        project_holder.clear_widgets()

        for project in content:
            project_holder.add_widget(ProjectField(id=project.id, name=project.name))
