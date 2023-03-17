import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

def test_space_compress():
    assert sh.space_compress('word             word') == 'word word', "Failed multiple spaces"

@pytest.mark.xfail
def test_failing():
    assert sh.space_compress('word!' ) == 'word'

@pytest.mark.skip
def test_skip():
    assert False

#@pytest.mark.skipif(sys.platform == 'win32', reason = "OS runs on win32")
#def test_platform():
#    print(sys.platform)
#    print("My platform is", sys.platform)
#    assert False

def test_circleci_change():
    assert True, "Just a test to force a change"
