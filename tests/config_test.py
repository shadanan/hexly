import hexly as hl


def test_decrease_max_rows():
    hl.set_max_rows(10)
    hv = hl.HexView(bytes(range(0x100)))
    actual = hv._repr_html_()
    expected = 10
    assert actual.count('<th class="rh">') == expected
    hl.set_max_rows(0x100)
