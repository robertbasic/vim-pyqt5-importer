if exists('g:pyqt5importer_plugin_loaded') || &cp
    finish
endif
let g:pyqt5importer_plugin_loaded = 1

let g:pyqt5importer_plugin_path = expand('<sfile>:p:h')

let g:pyqt5importer_pyqt5_json_path = expand('~/.vim/pyqt5.json')

call pyqt5importer#SetupPyImports()

command! -nargs=0 PyQt5ImportClass call pyqt5importer#pyqt5ImportClass()
