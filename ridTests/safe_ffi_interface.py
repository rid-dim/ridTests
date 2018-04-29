########################################################################################################################
#
# pySafe - C FFI interface
#
# The purpose of this file is to parse and define the function signatures and structures defined in
#  ./safe_c_ffi_funcs.h   -> the header signatures
#  ./safe_c_datatypes.h   -> the data structures
#
# This can be done inline, but at present is done from the 'header' files for cleanliness of code and to facilitate
# interoperation with the utility that can generate these files.
#
# The current intended use of this file is to be imported in its entirety by 'interface.py' only.  Nothing in this file
# should be *directly* available to the end-user
#
# The current implementation is the 'ABI - Inline' mode of cffi operation.  As we benchmark performance, it may be
# useful to switch it to actually compiling a library rather than doing it all in Python. See
# https://cffi.readthedocs.io/en/latest/overview.html#simple-example-abi-level-in-line
#
########################################################################################################################
import ridTests.localization
from cffi import FFI
ffi = FFI()



if __name__=='__main__':
    print('safe_ffi_interface.py loaded')
