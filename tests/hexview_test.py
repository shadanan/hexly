import hexly as hl


def test_hv_empty_data_succeeds():
    hv = hl.HexView(b"")
    hv._repr_html_()


def test_hv_one_bytes_succeeds():
    hv = hl.HexView(b"\x00")
    hv._repr_html_()


def test_hv_contains_expected_row_headers():
    hv = hl.HexView(bytes(range(0x100)))
    actual = hv._repr_html_()
    for header in range(0, 0x100, 0x10):
        expected = f'<th class="rh">{header:02X}</th>'
        assert expected in actual


def test_hv_slice_contains_expected_row_headers():
    hv = hl.HexView(bytes(range(0x100)))
    actual = hv[0x10:0x50]._repr_html_()
    for header in range(0x10, 0x50, 0x10):
        expected = f'<th class="rh">{header:02X}</th>'
        assert expected in actual


def test_hv_contains_expected_column_headers():
    hv = hl.HexView(bytes(range(0x100)))
    actual = hv._repr_html_()
    for header in range(0, 0x10):
        expected = f"<th>{header:02X}</th>"
        assert expected in actual


def test_empty_hv_contains_single_row_header():
    hv = hl.HexView(b"")
    actual = hv._repr_html_()
    expected = '<th class="rh">00</th>'
    assert expected in actual


def test_very_large_hv_prints_max_rows_and_warning_footer():
    hv = hl.HexView(bytes(list(range(0x100)) * 0x100))
    actual = hv._repr_html_()

    assert actual.count('<th class="rh">') == 0x100

    expected = "additional rows not shown..."
    assert expected in actual


def test_hv_contains_ascii_name():
    hv = hl.HexView(bytes(range(0x100)))
    actual = hv._repr_html_()
    expected = "ASCII"
    assert expected in actual


def test_hv_ascii_encoding_contains_161_unprintable_characters():
    hv = hl.HexView(bytes(range(0x100)))
    actual = hv._repr_html_()
    expected = 161
    assert actual.count('class="up"') == expected


def test_hv_ibm437_encoding_contains_ibm437_name():
    hv = hl.HexView(bytes(range(0x100)), encoding=hl.IBM437)
    actual = hv._repr_html_()
    expected = "IBM437"
    assert expected in actual


def test_hv_ibm437_encoding_contains_2_unprintable_characters():
    hv = hl.HexView(bytes(range(0x100)), encoding=hl.IBM437)
    actual = hv._repr_html_()
    expected = 2
    assert actual.count('class="up"') == expected


def test_hv_ibm850_encoding_contains_ibm850_name():
    hv = hl.HexView(bytes(range(0x100)), encoding=hl.IBM850)
    actual = hv._repr_html_()
    expected = "IBM850"
    assert expected in actual


def test_hv_windows1252_encoding_contains_windows1252_name():
    hv = hl.HexView(bytes(range(0x100)), encoding=hl.WINDOWS_1252)
    actual = hv._repr_html_()
    expected = "Windows-1252"
    assert expected in actual


def test_hv_hexly_encoding_contains_hexly_name():
    hv = hl.HexView(bytes(range(0x100)), encoding=hl.HEXLY)
    actual = hv._repr_html_()
    expected = "HEXLY"
    assert expected in actual


def test_hv_hexly_encoding_contains_no_unprintable_characters():
    hv = hl.HexView(bytes(range(0x100)), encoding=hl.HEXLY)
    actual = hv._repr_html_()
    assert 'class="up"' not in actual
