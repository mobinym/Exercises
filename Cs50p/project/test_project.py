import project
import pytest

def test_sum():
    assert project.sum(10,20)==30
    assert project.sum(10,2)==12
    assert project.sum(1,2)==3
    assert project.sum(1,4)==5
    assert project.sum(1,10)==11
    assert project.sum(12,10)==22
    assert project.sum(12,-10)==2

def test_mul():
    assert project.mul(10,2)==20
def test_search_to_list():
    assert project.search_to_list([10,20,30,40,50],40)==[10,20,30,40,50]
    assert project.search_to_list([10,20,30,40,50],1)==False
