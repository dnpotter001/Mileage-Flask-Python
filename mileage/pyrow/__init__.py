

#from .pyrow import pyrow
import usb.core
import usb.util
from usb import USBError
from  . import csafe_cmd
from .pyrow import pyrow
import datetime
import time
import sys


C2_VENDOR_ID = 0x17a4
MIN_FRAME_GAP = .050 #in seconds
INTERFACE = 0

def find():
    ergs = usb.core.find(find_all=True, idVendor=C2_VENDOR_ID)
    if ergs is None:
        raise ValueError('Ergs not found')
    return ergs


# print(find())
