from betterLogger import ClassWithLogger
from kivy.graphics import Color
from kivy.properties import ColorProperty, NumericProperty
from kivy.uix.layout import Layout
from kivy.uix.relativelayout import RelativeLayout


class Page(ClassWithLogger, RelativeLayout):
    bg_bg_color: Color = ColorProperty()
    bg_fg_color: Color = ColorProperty()
    bg_fg_offset: int = NumericProperty()

    def __init__(self, **kwargs):
        ClassWithLogger.__init__(self)
        RelativeLayout.__init__(self, **kwargs)
