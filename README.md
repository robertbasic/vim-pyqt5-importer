vim-pyqt5-importer
==================

A VIM plugin to help with importing PyQt5 classes.

Usage
=====

Call `:PyQt5ImportClass` over a word that represents a PyQt5 class.

Requirements
============

A JSON dump file created by [pyqt5-dumper](https://github.com/robertbasic/pyqt5-dumper).

Put that JSON file somewhere and do a `let g:pyqt5importer_pyqt5_json_path="/path/to/dump.json"` to tell the plugin where the JSON file is.

By default it will look for it in `~/.vim/pyqt5.json`.

Installation
============

Using [vim-plug](https://github.com/junegunn/vim-plug):

`Plug 'robertbasic/vim-pyqt5-importer'`
