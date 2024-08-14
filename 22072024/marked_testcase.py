"""
What is marking ?
If we want to execute some TCs like to perform smoke testing.
In that case we mark TCs "@pytest.mark.smoke"
so all smoke TCs will execute by using below command.
pytest -m "smoke" filepath or blank  ( In case of blank it will execute all smoke TCs in project)
"""
import pytest


@pytest.mark.smoke
def test_sub0():
    assert 0 - 0 == 0


@pytest.mark.regression
def test_sub1():
    assert 1 - 1 == 0


@pytest.mark.smoke
def test_sub2():
    assert 2 - 2 == 0


@pytest.mark.sanity
def test_sub3():
    assert 1 - 0 == 0


@pytest.mark.skip(reason="Not working, skip it")
def test_sub4():
    assert 0 - 0 == 0
