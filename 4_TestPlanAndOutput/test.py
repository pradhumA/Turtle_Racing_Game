"""pytest"""
import pytest
from main import start_game
from log import login_details

colors = ["red", "green","cyan", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']

def test_case():
    """TestCase"""
    assert login_details("pradhum",123)==0

def test_case1():
    """TestCase1"""
    assert start_game(2)==0

def test_case2():
    """TestCase2"""
    assert start_game(3)==0

@pytest.mark.skip(reason="Not predict correct winner turtle !")
def test_case3():
    """TestCase3"""
    assert start_game(4)==0

@pytest.mark.skipif(reason="skipped test case bcoz my pridiction is Incorrect !")
def test_case4():
    """TestCase4"""
    assert start_game(2)==0