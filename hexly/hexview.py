from dataclasses import dataclass, field

from .config import config
from .encoding import ASCII, Encoding
from .templates import CELL, COLUMN, CSS, HEADER, JS, ROW, TABLE


@dataclass
class HexView:
    data: bytes
    columns: int = field(default=16, kw_only=True)
    encoding: Encoding = field(default_factory=lambda: ASCII, kw_only=True)
    _offset: int = field(default=0, init=False, compare=False)

    def _hex_cell_html(self, hlid: int, index: int):
        if index >= len(self.data):
            return "<td></td>"
        id = f"hl{hlid}h{index}"
        text = f"{self.data[index]:02X}"
        return CELL.format(hlid=hlid, id=id, classes="hc", index=index, text=text)

    def _text_cell_html(self, hlid: int, index: int):
        if index >= len(self.data):
            return "<td></td>"
        id = f"hl{hlid}t{index}"
        text, classes = ".", "up"
        if self.data[index] in self.encoding:
            text, classes = self.encoding[self.data[index]], "tc"
        return CELL.format(hlid=hlid, id=id, classes=classes, index=index, text=text)

    def _row_header(self, row: int) -> int:
        return row * self.columns + self._offset

    def _row_html(self, hlid: int, row: int):
        start, end = row * self.columns, (row + 1) * self.columns
        header = f"{self._row_header(row):02X}"
        hex_cells = "".join([self._hex_cell_html(hlid, i) for i in range(start, end)])
        text_cells = "".join([self._text_cell_html(hlid, i) for i in range(start, end)])
        return ROW.format(header=header, hex_cells=hex_cells, text_cells=text_cells)

    def _column_html(self):
        return COLUMN.format(
            headers="".join([f"<th>{i:02X}</th>" for i in range(self.columns)]),
            columns=self.columns,
            encoding=self.encoding.name,
        )

    def _repr_html_(self):
        hlid = config.get_unique_table_id()

        total_rows = max(-(len(self.data) // -self.columns), 1)
        rows = min(total_rows, config.max_rows)
        remainder = total_rows - rows

        content = self._column_html()
        content += "".join([self._row_html(hlid, row) for row in range(rows)])

        header = HEADER.format(css=CSS, js=JS.format(hlid=hlid))
        footer = f"{remainder} additional rows not shown..." if remainder > 0 else ""

        return TABLE.format(hlid=hlid, header=header, content=content, footer=footer)

    def __getitem__(self, key: slice) -> "HexView":
        hv = HexView(
            self.data[key],
            columns=self.columns,
            encoding=self.encoding,
        )
        hv._offset = key.start
        return hv
