from kivy.properties import NumericProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget


class SameSizeListHolderLayout(RelativeLayout):
    child_height: int = NumericProperty(100)

    def __init__(self, **kwargs):
        RelativeLayout.__init__(self, **kwargs)
        self.size_hint_y = None

    def do_layout(self, *args):
        y = 0

        child: Widget
        for child in self.children:
            child.width = self.width
            child.height = self.child_height
            child.x = 0
            child.y = y

            y += self.child_height

        self.height = y
