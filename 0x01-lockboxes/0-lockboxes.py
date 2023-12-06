#!/usr/bin/python3
""" This oves the Lockboxes Challenge using recursion."""


def open_box(boxes, box_key, avail_keys):
    """ This opens a box and adds all new keys to the available keys. """
    for key in boxes[box_key]:
        if key in avail_keys:
            continue
        avail_keys.append(key)
        if key < len(boxes):
            open_box(boxes, key, avail_keys)


def canUnlockAll(boxes):
    """ determines if all the boxes can be opened. """
    avail_keys = []
    for box in range(len(boxes)):
        if box == 0 or box in avail_keys:
            open_box(boxes, box, avail_keys)
        else:
            return False
    return True
