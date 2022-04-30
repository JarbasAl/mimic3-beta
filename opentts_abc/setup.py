#!/usr/bin/env python3
# Copyright 2022 Mycroft AI Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from collections import defaultdict
from pathlib import Path

import setuptools
from setuptools import setup

setup(
    name="opentts_abc",
    version="0.1",
    author="Michael Hansen",
    author_email="michael.hansen@mycroft.ai",
    license="AGPLv3+",
    packages=["opentts_abc"],
    keywords="mycroft tts speech mimic",
)
