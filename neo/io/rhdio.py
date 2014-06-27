# -*- coding: utf-8 -*-
"""
Class for reading .rhd files created by Intan Tech's gui acquisition interface.

Depends on: none

Supported: Read

Author: Tom Gillespie

"""

# needed for python 3 compatibility
from __future__ import absolute_import

# note neo.core needs only numpy and quantities
import numpy as np
import quantities as pq

# I need to subclass BaseIO
from neo.io.baseio import BaseIO

class RhdIO(BaseIO):
    """
    Class for reading .rhd files created by Intan Tech's gui acquisition interface.

    Usage:
        >>> from neo import io
        >>> r = io.RhdIO(filename='myfile.rhd')

    """

    is_readable = True
    is_writeable = False

    supported_objects = [Segment, AnalogSignal]
    readable_objects = [Segment, AnalogSignal]
    writeable_objects = []

    has_header = True
    is_streameable = False #  hrm??
