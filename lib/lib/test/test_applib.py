""" Tests for applib """
import applib.lib as lib


def test_get_even_value():
    value = lib.get_even_value()
    assert value % 2 == 0
