import openpyxl
from openpyxl.utils import get_column_letter

def copy_row_to_rows(sheet, start_row, finish_row, src_row):

    for row in range(start_row, finish_row+1):
        copy_row(sheet, row, src_row)

def copy_row(sheet, tgt_row, src_row):

    tgt_range = '{}:{}'.format(tgt_row, tgt_row)

    for col in range(1, num_styled_cols(sheet, tgt_range)):
        col_letter = get_column_letter(col)
        sheet['{}{}'.format(col_letter, tgt_row)]._style = sheet['{}{}'.format(col_letter, src_row)]._style
