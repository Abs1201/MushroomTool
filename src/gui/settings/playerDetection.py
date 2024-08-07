import tkinter as tk
from src.gui.interfaces import LabelFrame, Frame
from src.common.interfaces import Configurable


class PlayerDetection(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Detection', **kwargs)

        self.playerDetection_settings = PlayerDetectionSettings('playerDetection')
        self.auto_return = tk.BooleanVar(value=self.playerDetection_settings.get('Auto-return'))

        return_row = Frame(self)
        return_row.pack(side=tk.TOP, fill='x', expand=True, pady=5, padx=5)
        check = tk.Checkbutton(
            return_row,
            variable=self.auto_return,
            text='Auto-return',
            command=self._on_change
        )
        check.pack()

    def _on_change(self):
        self.playerDetection_settings.set('Auto-return', self.auto_return.get())
        self.playerDetection_settings.save_config()


class PlayerDetectionSettings(Configurable):
    DEFAULT_CONFIG = {
        'Auto-return': True
    }

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        assert key in self.config
        self.config[key] = value
