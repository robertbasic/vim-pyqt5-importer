function! pyqt5importer#pyqt5ImportClass()
python3 << endpython3
import vim
from pyqt5importer import importer
from pyqt5importer import packages

def import_class():

    current_class = vim.eval('expand("<cword>")')
    is_pyqt5_class = importer.is_pyqt5_class(current_class)

    if not is_pyqt5_class:
        print("%s is not a PyQt5 class." % (current_class))
        return

    current_buffer = vim.current.buffer
    buffer_range = current_buffer.range(1, len(current_buffer))

    import_lines = []
    last_import_line_number = 0
    for line_number in range(len(current_buffer)):
        current_range = current_buffer.range(line_number, line_number)
        for line in current_range:
            if importer.is_import_line(line):
                import_lines.append(line)
                last_import_line_number = line_number

    is_imported = importer.is_pyqt5_class_imported(current_class, import_lines)

    if is_imported:
        print("%s is already imported." % (current_class))
        return

    pyqt5_json_path = vim.eval('g:pyqt5importer_pyqt5_json_path')

    package = packages.find_class_package(current_class, pyqt5_json_path)

    if not package:
        print("No PyQt5 package found %s" % (current_class))
        return

    print("%s package found for %s" % (package, current_class))

    import_line = "from PyQt5.%s import %s" % (package, current_class)
    current_buffer.append(import_line, last_import_line_number)

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
