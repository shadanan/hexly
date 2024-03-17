import os

with open(os.path.join(os.path.dirname(__file__), "style.css")) as f:
    CSS = f.read()

JS = """
function highlight{hlid}(cellId) {{
  document.getElementById(`hl{hlid}h${{cellId}}`).classList.add("hl");
  document.getElementById(`hl{hlid}t${{cellId}}`).classList.add("hl");
}}
function unhighlight{hlid}(cellId) {{
  document.getElementById(`hl{hlid}h${{cellId}}`).classList.remove("hl");
  document.getElementById(`hl{hlid}t${{cellId}}`).classList.remove("hl");
}}
"""

HEADER = '<style>{css}</style><script type="text/javascript">{js}</script>'

TABLE = '{header}<table id="hl{hlid}" class="hexly">{content}</table>{footer}'

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
    'onMouseOver="highlight{hlid}({index})" '
    'onMouseOut="unhighlight{hlid}({index})">'
    "{text}"
    "</td>"
)
