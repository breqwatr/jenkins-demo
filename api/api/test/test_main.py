""" Tests for main.py """
import appapi.main as main


def test_index():
    """ Test that the index() function returns something without crashing """
    site_content = main.index()
    assert site_content

