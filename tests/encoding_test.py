import hexly.encoding as encoding


def test_ascii_encodes_correct_range():
    for i in range(0x00, 0x20):
        assert i not in encoding.ASCII
    for i in range(0x20, 0x7F):
        assert i in encoding.ASCII
    for i in range(0x7F, 0x100):
        assert i not in encoding.ASCII


def test_cp437_encodes_correct_range():
    assert 0x00 not in encoding.IBM437
    for i in range(0x01, 0xFF):
        assert i in encoding.IBM437
    assert 0xFF not in encoding.IBM437


def test_cp850_encodes_correct_range():
    assert 0x00 not in encoding.IBM850
    for i in range(0x01, 0xFF):
        assert i in encoding.IBM850
    assert 0xFF not in encoding.IBM850


def test_windows1252_encodes_correct_range():
    for i in range(0x20):
        assert i not in encoding.WINDOWS_1252
    for i in range(0x20, 0x7F):
        assert i in encoding.WINDOWS_1252
    assert 0x80 in encoding.WINDOWS_1252
    assert 0x81 not in encoding.WINDOWS_1252
    for i in range(0x82, 0x8D):
        assert i in encoding.WINDOWS_1252
    assert 0x8D not in encoding.WINDOWS_1252
    assert 0x8E in encoding.WINDOWS_1252
    assert 0x8F not in encoding.WINDOWS_1252
    assert 0x90 not in encoding.WINDOWS_1252
    for i in range(0x91, 0x9D):
        assert i in encoding.WINDOWS_1252
    assert 0x9D not in encoding.WINDOWS_1252
    assert 0x9E in encoding.WINDOWS_1252
    assert 0x9F in encoding.WINDOWS_1252
    assert 0xA0 not in encoding.WINDOWS_1252
    for i in range(0xA1, 0x100):
        assert i in encoding.WINDOWS_1252


def test_hexly_encodes_correct_range():
    for i in range(0x100):
        assert i in encoding.HEXLY
