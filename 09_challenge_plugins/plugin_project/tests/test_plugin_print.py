from io import StringIO
from unittest.mock import patch
from plugins.plugin_print import PluginPrint

def test_execute():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        message = "Hello, World!"
        plugin = PluginPrint(message)
        plugin.execute()
        assert mock_stdout.getvalue().strip() == message
