import openpyxl
from openpyxl.utils import get_column_letter

def copy_row(sheet, src_row, tgt_row):

    tgt_range = '{}:{}'.format(tgt_row, tgt_row)
    # src_range = '{}:{}'.format(src_row)

    for col in range(1, len([cell._style for cell in sheet[tgt_range]])):
        col_letter = get_column_letter(col)
        sheet['{}{}'.format(col_letter, tgt_row)]._style = sheet['{}{}'.format(col_letter, src_row)]._style
