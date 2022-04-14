from betterLogger import ClassWithLogger
from kivy.app import App
from kivy.lang import Builder

# noinspection PyUnresolvedReferences
from src.widgets.pages.projectSearchPage import ProjectSearchPage

# noinspection PyUnresolvedReferences
from src.widgets.fields.searchBoxField import SearchBoxField
# noinspection PyUnresolvedReferences
from src.widgets.fields.projectField import ProjectField

# noinspection PyUnresolvedReferences
from src.widgets.sameSizeListHolderLayout import SameSizeListHolderLayout


class GjDataStorageSystemApp(App, ClassWithLogger):
    def __init__(self, **kwargs):
        ClassWithLogger.__init__(self)
        App.__init__(self, **kwargs)

    def build(self):
        Builder.load_file("resources/widgetStyles.kv")
        return Builder.load_file("resources/pageStyles.kv")
