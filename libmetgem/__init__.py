"""
    A library for molecular networking based on MS/MS spectra.
"""

from .common import MZ, INTENSITY
from ._version import *

import numpy as np

def human_readable_data(data: np.ndarray) -> np.ndarray:
    """
        Normalize an MS/MS spectrum to the spectrum's maximum intensity and
        revert `filter_data` square-root process.
        
    Args:
        data: A 2D array representing an MS/MS spectrum.
        
    Returns:
        A copy of the array with intensities squared and normalised to maximum.
        
    See Also:
        filter_data
    
    """
    
    data = data.copy()
    data[:, INTENSITY] = data[:, INTENSITY] ** 2
    data[:, INTENSITY] = data[:, INTENSITY] / data[:, INTENSITY].max() * 100
    return data
