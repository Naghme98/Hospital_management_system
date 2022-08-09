from PyQt5.uic import compileUi


def comp(ui_path, py_path):
    compileUi(ui_path, open(py_path, 'w'))


if __name__ == "__main__":
    # comp('showdoctimesform.ui', 'showdoctimesform_form.py')
    comp('signup2_2.ui', 'signup2_2_form.py')
