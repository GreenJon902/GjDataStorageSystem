import abc

from betterLogger import ClassWithLogger
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class Tab(BoxLayout, abc.ABC, ClassWithLogger):
    tabName: str = StringProperty("Tab")

    def __init__(self, **kwargs):
        abc.ABC.__init__(self)
        ClassWithLogger.__init__(self)
        BoxLayout.__init__(self, **kwargs)
