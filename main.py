import PySimpleGUI as sg
from pathlib import Path
from data import images
import os

# GUI
if __name__ == '__main__':
    sg.theme('Brown Blue')

    filepath = sg.popup_get_file(title='OCRMyPdf', message='选择文件位置',
                                 file_types=(('PDF', '*.pdf'),), history=True,
                                 icon=images)

    if filepath is None:
        pass
    elif Path(filepath).is_file() and len(filepath) > 0:
        outfilepath = filepath.replace(".pdf", "_OCR.pdf")
        cmd = 'python -m ocrmypdf -l eng+chi_sim "'+ filepath + '" "' + outfilepath +'"'
        os.system(cmd)