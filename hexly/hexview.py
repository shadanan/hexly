from dataclasses import dataclass, field
from enum import Enum

from .config import config
from .encoding import ASCII, Encoding
from .templates import CELL, COLUMN, HEADER, ROW, TABLE


class CellType(Enum):
    HEX = "h"
    TEXT = "t"


@dataclass
class HexView:
    data: bytes
    columns: int = field(default=16, kw_only=True)
    encoding: Encoding = field(default_factory=lambda: ASCII, kw_only=True)
    _offset: int = field(default=0, init=False, compare=False)

    def _cell_html(self, hv: int, index: int, ct: CellType):
        id = f"hv{hv}{ct.value}{index}"
        classes = f"{ct.value}c"
        if ct == CellType.HEX:
            text = f"{self.data[index]:02X}"
        elif self.data[index] in self.encoding:
            text = self.encoding.code[self.data[index]]
        else:
            text = "."
            classes = "up"
        return CELL.format(id=id, classes=classes, hv=hv, index=index, text=text)

    def _row_header(self, row: int) -> int:
        return row * self.columns + self._offset

    def _row_html(self, hv: int, row: int):
        start = row * self.columns
        end = min((row + 1) * self.columns, len(self.data))
        header = f"{self._row_header(row):02X}"
        empty_cells = ["<td></td>"] * (self.columns - (end - start))
        hex_cells = "".join(
            [self._cell_html(hv, i, CellType.HEX) for i in range(start, end)]
            + empty_cells
        )
        text_cells = "".join(
            [self._cell_html(hv, i, CellType.TEXT) for i in range(start, end)]
            + empty_cells
        )
        return ROW.format(header=header, hex_cells=hex_cells, text_cells=text_cells)

    def _column_html(self):
        return COLUMN.format(
            headers="".join([f"<th>{i:02X}</th>" for i in range(self.columns)]),
            columns=self.columns,
            encoding=self.encoding.name,
        )

    def _repr_html_(self):
        hv_id = config.get_unique_table_id()

        total_rows = max(-(len(self.data) // -self.columns), 1)
        rows = min(total_rows, config.max_rows)
        remainder = total_rows - rows

        content = self._column_html()
        content += "".join([self._row_html(hv_id, row) for row in range(rows)])

        footer = f"{remainder} additional rows not shown..." if remainder > 0 else ""

        return TABLE.format(id=hv_id, header=HEADER, content=content, footer=footer)

    def __getitem__(self, key: slice) -> "HexView":
        hv = HexView(
            self.data[key],
            columns=self.columns,
            encoding=self.encoding,
        )
        hv._offset = key.start
        return hv
