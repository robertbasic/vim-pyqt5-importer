import re
import itertools

def is_pyqt5_class(class_name):
    pattern = re.compile("(Q[A-Z]{1})([a-zA-Z]+)")
    match = pattern.match(class_name)

    return match is not None

def is_import_line(line):
    pattern = re.compile("^import|^from")
    match = pattern.search(line)

    return match is not None

def is_pyqt5_class_imported(class_name, import_lines):
    imported_classes = get_imported_classes(import_lines)

    pattern = re.compile("\\b" + class_name + "\\b")
    matches = [pattern.match(ic) for ic in imported_classes]

    matches = list(map(lambda x: True if x is not None else False, matches))

    return True in matches

def get_imported_classes(import_lines):
    pattern = re.compile("(Q[A-Z]{1}[a-zA-Z]+)")
    matches = [pattern.findall(line) for line in import_lines]

    return set(itertools.chain.from_iterable(matches))
