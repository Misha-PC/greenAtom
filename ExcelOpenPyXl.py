import openpyxl
import openpyxl.styles.numbers
from config import header, column_type, file_path, sheet_name
from BaseAppException import BaseAppException

column_type_code = {
    'finance': 44,
    'percent': 9,
    'date': 14,
    'num': 2
}


class NoSheetError(BaseAppException):
    pass


class CellFormatException(BaseAppException):
    pass


def prepear_data_to_excel(usd: list, eur: list, header: list) -> list:
    """
    :param usd: list with dollar currencies rate
    :param eur: list with euro currencies rate
    :param header: list with column names
    :return: list
    """
    output = list()
    output.append(header)

    lines_count = max(len(usd), len(eur))

    for i in range(lines_count):
        if len(usd) > i and len(eur):
            output.append(usd[i] + [''] + eur[i] + [''] + [float(eur[i][1]) / float(usd[i][1])])
        elif len(usd) > i:
            output.append(usd[i])
        else:
            output.append(eur[i])

    return [output, lines_count + 1]


def write_array_to_excel(content: list, file_path: str = "output.xlsx"):
    """
    :param content: list with table content
    :param file_path:
    :return: None
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in content:
        ws.append(row)

    for type_ in column_type.keys():
        for col in column_type[type_]:
            for row in range(1, 30):
                style = openpyxl.styles.numbers.BUILTIN_FORMATS[column_type_code[type_]]
                ws.cell(column=col, row=row).number_format = style

    for i in ['A', 'D']:
        ws.column_dimensions[i].width = 12

    for i in ['B', 'E']:
        ws.column_dimensions[i].width = 10

    for i in ['G', 'C', 'F']:
        ws.column_dimensions[i].width = 11

    wb.save(filename=file_path)


def check_cell_type(file_pah: str):
    """
    :param file_pah:
    :return: True if type of cells corresponds to the required, else raise CellFormatException
    """
    wb = openpyxl.load_workbook(filename=file_pah)
    if not sheet_name in wb.sheetnames:
        raise NoSheetError(f"No '{sheet_name}' from '{file_pah}'")

    ws = wb[sheet_name]

    for type_ in column_type.keys():
        for col in column_type[type_]:
            for row in range(1, 30):
                style = openpyxl.styles.numbers.BUILTIN_FORMATS[column_type_code[type_]]
                if ws.cell(column=col, row=row).number_format != style:
                    raise CellFormatException(f"Cell[{col}, {row}] format is not {style}")
    return True


if __name__ == '__main__':
    check_cell_type(file_path)