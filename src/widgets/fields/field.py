from typing import Optional

from betterLogger import ClassWithLogger
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.input import MotionEvent
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.relativelayout import RelativeLayout


class Field(RelativeLayout):
    mouse_over: bool = BooleanProperty(False)
    focused: bool = BooleanProperty(False)

    def __init__(self, **kwargs):
        RelativeLayout.__init__(self, **kwargs)

        Window.bind(mouse_pos=self._on_mouse_move)

        focusHandler.add_field(self)

    def _on_mouse_move(self, _window, pos):
        relative_pos = self.to_widget(*pos)
        if 0 <= relative_pos[0] < self.width and 0 <= relative_pos[1] < self.height:
            self.mouse_over = True
        else:
            self.mouse_over = False


class _FocusHandler(EventDispatcher, ClassWithLogger):
    _current_focused: Optional[Field] = ObjectProperty(allownone=True)
    fields: list[Field]

    def __init__(self, **kwargs):
        EventDispatcher.__init__(self, **kwargs)
        ClassWithLogger.__init__(self)
        self.fields = list()

        Window.bind(on_touch_up=self.on_touch_up)

    def on__current_focused(self, _instance, value):
        self.log_debug(f"Focus switched to {value}")
        for field in self.fields:
            if field == value:
                field.focused = True
            else:
                field.focused = False

    def current_focus_is(self, field: Field):
        return self._current_focused == field

    def add_field(self, field: Field):
        self.fields.append(field)

    def on_touch_up(self, _instance, touch: MotionEvent):
        if len(touch.grab_list) == 0:
            for field in self.fields:
                if field.collide_point(*field.to_parent(*field.to_widget(*touch.pos))):
                    self._current_focused = field
                    return
            self._current_focused = None


focusHandler = _FocusHandler()
