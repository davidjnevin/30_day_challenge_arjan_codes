from .plugin_base import PluginBase

class PluginPrint(PluginBase):
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(self.message)
