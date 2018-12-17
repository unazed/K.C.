"""This program is for a special person called Kaci."""

# from __future__ import braces # I'm using this import because
                                # it describes the forbidden
                                # nature and short-lived
                                # span of our relationship
import ctypes  # I'm using `ctypes` because it relates to my 
               # relationship between me and Kaci: foreign.
import this  # I'm using `this` because it describes the 
             # literary beauty and yet inherent uselessness 
             # in practicality between me and Kaci.
import time  # I'm using `time` to represent the brevity of
             # our relationship.
try:
    import kacis_grades
except ImportError as FoundationFailure:
    "I'm using this to represent the point of failure"
    "in our relationship."


def love(giver, receiver):
    giver.give(receiver.receive_fd)
    return receiver.status


while "kaci" != "interested":
    time.sleep(60 * 60 * 24)  # another day, another range
                              # of emotions

love("unazed", "kaci")
# this line is never reached, and if it is:
# it will never run successfully

MessageBoxA = ctypes.windll.user32.MessageBoxA
MessageBoxA.argtypes = (ctypes.c_voidp,
                        ctypes.POINTER(ctypes.c_char),
                        ctypes.POINTER(ctypes.c_char),
                        ctypes.c_uint)
MessageBoxA.retype = ctypes.c_int
window_text = b"ily kaci"
p_window_text = ctypes.create_string_buffer(len(window_text))
p_window_text.value = window_text
caption_text = b"<3"
p_caption_text = ctypes.create_string_buffer(len(caption_text))
p_caption_text.value = caption_text
MessageBoxA(None, p_window_text, p_caption_text, 0x0)

ExitWindowsEx = ctypes.windll.user32.ExitWindowsEx
ExitWindowsEx.argtypes = (ctypes.c_uint, ctypes.c_long)
ExitWindowsEx.restype = ctypes.c_int
ExitWindowsEx(0x00400000, 0x0)
# goodbye, world.
