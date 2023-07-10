from decimal import Decimal
import importlib
from importlib.util import module_from_spec, spec_from_file_location
from typing import Protocol
import os


class Plugin(Protocol):
    @staticmethod
    def get_payment_method() -> str:
        ...

    @staticmethod
    def process_payment(total: Decimal) -> None:
        ...


PLUGINS: dict[str, Plugin] = {}

def import_mmodule(name: str) -> Plugin:
    """Imports a module given a name."""
    return importlib.import_module(name) # type: ignore

def load_plugins_from_folder(folder: str) -> None:
    """loads all modules from a folder."""
    for root, _, files in os.walk(folder):
        for file in files:
            print(file)
            if not file.endswith(".py"):
                continue
            module_name = file[:-3]
            # module_name = file.splitext[0]
            module_path = os.path.join(root, file)
            spec = spec_from_file_location(module_name, module_path)
            if (spec):
                module: Plugin = module_from_spec(spec) # type: ignore
                spec.loader.exec_module(module) # type: ignore
                PLUGINS[module.get_payment_method()] = module
def get_plugin(name: str) -> Plugin:
    """Gets a plugin by name."""
    return PLUGINS[name]

def plugin_exists(name: str):
    """Checks if the plugin exists."""
    return name in PLUGINS

def all_plugins() -> list[str]:
    """Gets all plugin names."""
    return list(PLUGINS.keys())
