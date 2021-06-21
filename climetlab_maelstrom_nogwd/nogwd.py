#!/usr/bin/env python3# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset
from climetlab.normalize import normalize_args

__version__ = "0.1.0"

URL = "https://storage.ecmwf.europeanweather.cloud"

PATTERN = "{url}/NOGWD_L91_PUBLIC/nc/{date}.nc"

class nogwd(Dataset):
    name = None
    home_page = "-"
    licence = "-"
    documentation = "-"
    citation = "-"

    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://github.com/ecmwf-lab/climetlab_maelstrom_nogwd/LICENSE"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    def __init__(self, dates):
        self.dates = dates

    # @normalize_args(parameter=["tp", "t2m"])
    def _load(self):
        request = dict(url=URL, date=self.dates)
        self.source = cml.load_source("url-pattern", PATTERN, request)
