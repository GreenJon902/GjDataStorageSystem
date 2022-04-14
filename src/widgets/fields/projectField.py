from kivy.properties import StringProperty, NumericProperty

from src.projectloader import Project
from src.widgets.fields.field import Field


class ProjectField(Field):
    id: int = NumericProperty()
    name: str = StringProperty()
