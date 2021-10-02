import enum

class RDPDATATYPE(enum.Enum):
	VIDEO = "VIDEO"
	KEYSCAN = 'KEYSCAN'
	KEYUNICODE = 'KEYUNICODE'
	MOUSE = 'MOUSE'
	CLIPBOARD_READY = 'CLIPBOARD_READY'
	CLIPBOARD_DATA_TXT = 'CLIPBOARD_DATA_TXT'
	CLIPBOARD_CONSUMED = 'CLIPBOARD_CONSUMED'

from aardwolf.commons.queuedata.video import RDP_VIDEO
from aardwolf.commons.queuedata.keyboard import RDP_KEYBOARD_SCANCODE, RDP_KEYBOARD_UNICODE
from aardwolf.commons.queuedata.mouse import RDP_MOUSE
from aardwolf.commons.queuedata.clipboard import RDP_CLIPBOARD_READY, RDP_CLIPBOARD_DATA_TXT, RDP_CLIPBOARD_CONSUMED

