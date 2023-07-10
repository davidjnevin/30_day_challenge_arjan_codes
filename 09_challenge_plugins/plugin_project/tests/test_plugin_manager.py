import pytest
from plugin_manager import PluginManager
from plugins.plugin_base import PluginBase
from plugins.plugin_print import PluginPrint

def test_register_plugin():
    manager = PluginManager()
    plugin = PluginPrint("Test message")
    manager.register_plugin(plugin)
    assert plugin in manager.plugins

def test_register_invalid_plugin():
    manager = PluginManager()
    with pytest.raises(ValueError):
        manager.register_plugin("Invalid plugin")
