from tkinter_handler import TkinterHandler
from dicom_table import DicomTable
import file_helper as FileHelper

tkinter = TkinterHandler()

directory_path = tkinter.draw_explorer()
print(directory_path)
all_files = FileHelper.list_all_files(directory_path)
dicom_table = DicomTable.from_files(all_files)

tkinter.draw_table(dicom_table.get_headers(),dicom_table.get_rows())