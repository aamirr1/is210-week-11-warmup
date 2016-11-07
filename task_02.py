#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Warm-up task 2"""

import time


class Snapshot(object):
    """
    This is a new class
    """

    def __init__(self, created=None):
        if created is None:
            created = int(time.time())

        self.created = created
