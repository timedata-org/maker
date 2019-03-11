import threading, time, tkinter as tk
from . import grounds


class Bang(tk.Button):
    def __init__(self, master, text,
                 off='white', on='yellow', delay=0.25, **kwds):
        super().__init__(master, text=text, state=tk.DISABLED, **kwds)
        self['disabledforeground'] = self['fg']
        self.colors = off, on
        self.delay = delay
        self.lock = threading.RLock()
        self._state = True
        self.state = False

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s):
        with self.lock:
            if s != self._state:
                self._state = s
                grounds.set_bg(self, self.colors[s])

    def _after(self, delay):
        self.after(int(1000 * delay), self._target)

    def bang(self):
        with self.lock:
            self.target_time = time.time() + self.delay
            if not self.state:
                self.state = True
                self._after(self.delay)

    def _target(self):
        with self.lock:
            remains = self.target_time - time.time()
            if remains <= 0:
                self.state = False
            else:
                self._after(remains)