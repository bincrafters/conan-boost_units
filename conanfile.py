#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostUnitsConan(base.BoostBaseConan):
    name = "boost_units"
    url = "https://github.com/bincrafters/conan-boost_units"
    lib_short_names = ["units"]
    header_only_libs = ["units"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_io",
        "boost_lambda",
        "boost_math",
        "boost_mpl",
        "boost_preprocessor",
        "boost_serialization",
        "boost_static_assert",
        "boost_type_traits",
        "boost_typeof"
    ]
