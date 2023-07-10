from plugins.plugin_base import PluginBase

class PluginManager:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin: PluginBase):
        if isinstance(plugin, PluginBase):
            self.plugins.append(plugin)
        else:
            raise ValueError("Invalid plugin")
