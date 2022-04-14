from kivy.properties import VariableListProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout


class PaddingLayout(RelativeLayout):
    padding = VariableListProperty(length=4)

    def do_layout(self, *args):
        FloatLayout.do_layout(self, *args, pos=(0, 0),
                              size=(self.width - (self.padding[0] + self.padding[2]),
                                    self.height - (self.padding[1] + self.padding[3])))
