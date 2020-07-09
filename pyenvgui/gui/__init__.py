from .. import pyenvapi

try:
    pyenv = pyenvapi.PyenvAPI()
except pyenvapi.exceptions.NotInstalledError:
    from .error_window import MainWindow
else:
    from .main_window import MainWindow