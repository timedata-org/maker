from . import grounds
import tkinter as tk


class ToggleButton(tk.Button):
    RELIEF = 'raised', 'sunken'

    def __init__(self, master, off, on, callback=None, **kwds):
        def command():
            self.state = not self.state

        super().__init__(master, command=command, **kwds)

        self.callback = callback
        self.texts = off, on
        self.colors = self['background'], self['foreground']
        self.state = False

    @property
    def state(self):
        return self._state

    @property
    def text(self):
        return self.texts[self._state]

    @state.setter
    def state(self, s):
        self._state = s
        text = self.text[s]
        bg, fg = self.colors[s], self.colors[not s]
        self.config(text=text, relief=self.RELIEF[s],
                    foreground=fg, activeforeground=fg,
                    background=bg, activebackground=bg)
        grounds.set_bg(self, bg)
        self.callback and self.callback(text)