# Copyright 2016 Autodesk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import moldesign.__main__

from moldesign import data
PACKAGEPATH = data.PACKAGEPATH

from moldesign import basemethods, compute, data, helpers, integrators, interfaces, logs
from moldesign import minimizers, models, orbitals, symmetry, ui, utils

# Make objects from these modules accessible at the top level
# (note that they all use __all__ to specify what gets exported)
from moldesign import atoms, biounits, converters, forcefield, geometry
from moldesign import molecule, tools, trajectory

from moldesign.atoms import *
from moldesign.biounits import *
from moldesign.converters import *
from moldesign.forcefield import *
from moldesign.geometry import *
from moldesign.molecule import *
from moldesign.tools import *
from moldesign.trajectory import *

# This is here primarily for sphinx's benefit
__all__ = (atoms.__all__ +
           biounits.__all__ +
           converters.__all__ +
           forcefield.__all__ +
           geometry.__all__ +
           molecule.__all__ +
           tools.__all__ +
           trajectory.__all__)

# Set warnings appropriately
# TODO: don't clobber user's or other package's settings!!!
import numpy as _np
import warnings as _warnings
_np.seterr(all='raise')
_warnings.simplefilter('error', _np.ComplexWarning)

# Other package metadata
__copyright__ = "Copyright 2016 Autodesk Inc."
__license__ = "Apache 2.0"
import os as _os
with open(_os.path.join(PACKAGEPATH, 'VERSION')) as versionfile:
    __version__ = versionfile.read().strip()