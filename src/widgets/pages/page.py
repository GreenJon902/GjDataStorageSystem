from betterLogger import ClassWithLogger
from kivy.uix.relativelayout import RelativeLayout


class Page(RelativeLayout, ClassWithLogger):
    def __init__(self, **kwargs):
        RelativeLayout.__init__(self, **kwargs)
        ClassWithLogger.__init__(self)
