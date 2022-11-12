import os
import sys
import pathlib
import importlib


DEFAULT_PRE_SCRIPT_FILE = ".pre-script.py"
PRE_SCRIPT_MODULE = "_pre_script"


def _run():
    if PRE_SCRIPT_MODULE in sys.modules:
        return
    
    pre_script_enabled = os.environ.get(
        "PRE_SCRIPT_ENABLED", ""
    ) in ("y", "yes", "1", "on", "true", "t", "on", "ok")
    if not pre_script_enabled:
        return

    pre_script_file = os.environ.get(
        "PRE_SCRIPT_FILE",
        DEFAULT_PRE_SCRIPT_FILE,
    )

    pre_script_file = pathlib.Path(pre_script_file)
    if pre_script_file.exists():
        file_loader = importlib.machinery.SourceFileLoader(
            PRE_SCRIPT_MODULE, str(pre_script_file),
        )
        spec = importlib.machinery.ModuleSpec(
            PRE_SCRIPT_MODULE, file_loader
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules[PRE_SCRIPT_MODULE] = module
        spec.loader.exec_module(module)

