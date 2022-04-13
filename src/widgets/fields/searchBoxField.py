import pprint

from kivy.graphics import InstructionGroup, Color, Rectangle

from src.widgets.fields.field import Field


class SearchBoxField(Field):
    def __init__(self, **kwargs):
        Field.__init__(self, **kwargs)
