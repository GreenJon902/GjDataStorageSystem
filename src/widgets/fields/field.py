from kivy.core.window import Window
from kivy.graphics.transformation import Matrix
from kivy.properties import BooleanProperty
from kivy.uix.relativelayout import RelativeLayout


class Field(RelativeLayout):
    mouse_over: bool = BooleanProperty(False)

    def __init__(self, **kwargs):
        RelativeLayout.__init__(self, **kwargs)

        Window.bind(mouse_pos=self._on_mouse_move)

    def _on_mouse_move(self, _window, pos):
        relative_pos = self.to_widget(*pos)
        if 0 <= relative_pos[0] < self.width and 0 <= relative_pos[1] < self.height:
            self.mouse_over = True
        else:
            self.mouse_over = False
