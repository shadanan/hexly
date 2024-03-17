import os

with open(os.path.join(os.path.dirname(__file__), "header.html")) as f:
    HEADER = f.read()

TABLE = '{header}<table id="hv{id}" class="hexly">{content}</table>{footer}'

COLUMN = (
    "<tr>"
    "<th></th>{headers}<th></th>"
    "<th colspan={columns}>DECODED TEXT ({encoding})</th>"
    "</tr>"
)

ROW = '<tr><th class="rh">{header}</th>{hex_cells}<td></td>{text_cells}</tr>'

CELL = (
    '<td id="{id}" '
    'class="{classes}" '
    'onMouseOver="highlight({hv}, {index})" '
    'onMouseOut="unhighlight({hv}, {index})">'
    "{text}"
    "</td>"
)
