import tkinter as tk
from src.gui.interfaces import LabelFrame, Frame
from src.common.interfaces import Configurable


class PlayerDetection(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Detection', **kwargs)

        self.playerDetection_settings = PlayerDetectionSettings('playerDetection')
        self.auto_return = tk.BooleanVar(value=self.playerDetection_settings.get('Auto-return'))
        # self.num_pets = tk.IntVar(value=self.pet_settings.get('Num pets'))

        return_row = Frame(self)
        return_row.pack(side=tk.TOP, fill='x', expand=True, pady=5, padx=5)
        check = tk.Checkbutton(
            return_row,
            variable=self.auto_return,
            text='Auto-return',
            command=self._on_change
        )
        check.pack()

        # num_row = Frame(self)
        # num_row.pack(side=tk.TOP, fill='x', expand=True, pady=(0, 5), padx=5)
        # label = tk.Label(num_row, text='Number of pets to feed:')
        # label.pack(side=tk.LEFT, padx=(0, 15))
        # radio_group = Frame(num_row)
        # radio_group.pack(side=tk.LEFT)
        # for i in range(1, 4):
        #     radio = tk.Radiobutton(
        #         radio_group,
        #         text=str(i),
        #         variable=self.num_pets,
        #         value=i,
        #         command=self._on_change
        #     )
        #     radio.pack(side=tk.LEFT, padx=(0, 10))

    def _on_change(self):
        self.playerDetection_settings.set('Auto-return', self.auto_return.get())
        # self.pet_settings.set('Num pets', self.num_pets.get())
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
