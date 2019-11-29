import pytest
from crypto_algs.Caesar import Caesar


def setup_module(module):
    # init_something()
    pass


def teardown_module(module):
    # teardown_something()
    pass


def test_zero_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 0) == b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c'


def test_single_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 1) == b'\xd2\x93\xd2\xb2\xd2\xbb\xd3\x84\xd3\x8d'


def test_256_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 256) ==\
           b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c'


def test_255_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 255) == \
           b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'


def test_42_shift():
    assert Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 42) == \
           b'\xfb\xbc\xfb\xdb\xfb\xe4\xfc\xad\xfc\xb6'
