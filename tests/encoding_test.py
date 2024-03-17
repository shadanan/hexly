import hexly.encoding as encoding


def test_ascii_encodes_printable_chars():
    for i in range(0x20, 0x7F):
        assert i in encoding.ASCII


def test_ascii_does_not_encode_unprintable_chars():
    for i in range(0x00, 0x20):
        assert i not in encoding.ASCII
    for i in range(0x7F, 0x100):
        assert i not in encoding.ASCII


def test_cp437_encodes_every_char_except_first_and_last():
    for i in range(0x01, 0xFF):
        assert i in encoding.CP437
    assert 0x00 not in encoding.CP437
    assert 0xFF not in encoding.CP437


def test_hexly_encodes_all_chars():
    for i in range(0x100):
        assert i in encoding.HEXLY
