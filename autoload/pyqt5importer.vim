function! pyqt5importer#pyqt5ImportClass()
python3 << endpython3
import vim
from pyqt5importer import importer

def import_class():

    current_class = vim.eval('expand("<cword>")')
    is_pyqt5_class = importer.is_pyqt5_class(current_class)

    if not is_pyqt5_class:
        print("%s is not a PyQt5 class." % (current_class))
        return

    current_buffer = vim.current.buffer
    buffer_range = current_buffer.range(1, len(current_buffer))

    import_lines = list(filter(importer.is_import_line, buffer_range))

    is_imported = importer.is_pyqt5_class_imported(current_class, import_lines)

    if is_imported:
        print("%s is already imported." % (current_class))
        return

import_class()

endpython3
endfunction

function! pyqt5importer#SetupPyImports()
python3 << endpython3
import os
import sys
import vim

python_plugin_path_loaded = int(vim.eval('exists("g:pyqt5importer_plugin_path_loaded")'))

if python_plugin_path_loaded == 0:
    vim.command("let g:pyqt5importer_plugin_path_loaded=1")

    plugin_path = vim.eval("g:pyqt5importer_plugin_path")
    python_plugin_path = os.path.abspath('%s/../lib' % (plugin_path))
    sys.path.append(python_plugin_path)

endpython3
endfunction
