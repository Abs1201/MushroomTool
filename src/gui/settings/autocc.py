import tkinter as tk
from src.gui.interfaces import LabelFrame, Frame
from src.common.interfaces import Configurable


class AutoCC(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Detection', **kwargs)

        self.autocc_settings = AutoCCSettings('autocc')
        self.autocc = tk.BooleanVar(value=self.autocc_settings.get('Auto-CC'))

        return_row = Frame(self)
        return_row.pack(side=tk.TOP, fill='x', expand=True, pady=5, padx=5)
        check = tk.Checkbutton(
            return_row,
            variable=self.autocc,
            text='Auto-CC',
            command=self._on_change
        )
        check.pack()

    def _on_change(self):
        self.autocc_settings.set('Auto-CC', self.autocc.get())
        self.autocc_settings.save_config()


class AutoCCSettings(Configurable):
    DEFAULT_CONFIG = {
        'Auto-CC': True
    }

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        assert key in self.config
        self.config[key] = value
