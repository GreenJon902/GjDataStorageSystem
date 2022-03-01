from betterLogger import ClassWithLogger
from kivy.app import App
from kivy.lang import Builder

# noinspection PyUnresolvedReferences
from widgets.tabLayout import TabLayout


class GjDataStorageSystemApp(App, ClassWithLogger):
    def __init__(self, **kwargs):
        ClassWithLogger.__init__(self)
        App.__init__(self, **kwargs)

    def build(self):

        return Builder.load_file("resources/kv.kv")
