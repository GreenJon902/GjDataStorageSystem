from src.widgets.fields.field import Field
from src.widgets.focusable import Focusable


class SearchBoxField(Field, Focusable):
    def __init__(self, **kwargs):
        Field.__init__(self, **kwargs)
        Focusable.__init__(self)
