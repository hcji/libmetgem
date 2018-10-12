"""
    Read spectra from MGF files.
"""

from ._loader import load_cython

from typing import Tuple
import numpy as np


__all__ = ('read', )

@load_cython
def read(filename: str, ignore_unknown: bool=False) -> Tuple[dict, np.ndarray]:
    """
        Read a file in `Mascot Generic Format (MGF)`_ and yields spectra.
    
    Args:
        filename: name of the file to read.
        ignore_unknown (optional): ignore unknown parameters, i.e. everything
            but PEPMASS, CHARGE, RTINSECONDS and MSLEVEL. This argument has no
            effect if `read` is not cythonized.
            
    Yields:
        params: Dictionary of spectrum's parameters
        data:   2D array containing spectrum data.
    
    .. _Mascot Generic Format (MGF):
        http://www.matrixscience.com/help/data_file_help.html
    
    """
    from pyteomics import mgf
    
    for entry in mgf.read(filename, convert_arrays=1, read_charges=True, dtype=np.float32):
        params = entry.get('params', {})
        for key in ('pepmass', 'charge'):
            if key in params and isinstance(params[key], (list, tuple)):
                params[key] = params[key][0]

        mz = entry.get('m/z array', None)
        intensity = entry.get('intensity array', None)
        yield params, np.column_stack((mz, intensity))