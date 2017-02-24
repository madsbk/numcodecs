# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division


import numpy as np
from numpy.testing import assert_raises


from numcodecs.pickles import Pickle
from numcodecs.tests.common import (check_config, check_repr,
                                    check_encode_decode_objects)


# object array with strings
# object array with mix strings / nans
# object array with mix of string, int, float
arrays = [
    np.array(['foo', 'bar', 'baz'] * 300, dtype=object),
    np.array([['foo', 'bar', np.nan]] * 300, dtype=object),
    np.array(['foo', 1.0, 2] * 300, dtype=object),
]

# non-object ndarrays
arrays_incompat = [
    np.arange(1000, dtype='i4'),
    np.array(['foo', 'bar', 'baz'] * 300),
]


def test_encode_errors():
    for arr in arrays_incompat:
        codec = Pickle()
        assert_raises(ValueError, codec.encode, arr)


def test_encode_decode():
    for arr in arrays:
        codec = Pickle()
        check_encode_decode_objects(arr, codec)


def test_config():
    codec = Pickle(protocol=-1)
    check_config(codec)


def test_repr():
    check_repr("Pickle(protocol=-1)")