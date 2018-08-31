# -*- coding: utf-8 -*-

"""Module module."""

from __future__ import absolute_import

import weakref

class Module(object):
    def __init__(self, id, uuid, modi):
        self._id = id
        self._uuid = uuid
        self._modi = weakref.ref(modi)
        self._category = str()
        self._type = str()
        self._topology = {
            'right': None,
            'up': None,
            'left': None,
            'down': None
        }

    @property
    def id(self):
        return self._id

    @property
    def uuid(self):
        return self._uuid

    @property
    def category(self):
        return self._category

    @property
    def type(self):
        return self._type

    @property
    def topology(self):
        return self._topology

    @property
    def right(self):
        return self._topology['right']

    @property
    def up(self):
        return self._topology['up']

    @property
    def left(self):
        return self._topology['left']

    @property
    def down(self):
        return self._topology['down']

class SetupModule(Module):
    def __init__(self, id, uuid, modi):
        super(SetupModule, self).__init__(id, uuid, modi)
        self._category = "setup"

class InputModule(Module):
    def __init__(self, id, uuid, modi):
        super(InputModule, self).__init__(id, uuid, modi)
        self._category = "input"
        self._properties = dict()
        
        for property_type in self.property_types:
            self._properties[property_type] = float()

class OutputModule(Module):
    def __init__(self, id, uuid, modi):
        super(OutputModule, self).__init__(id, uuid, modi)
        self._category = "output"
        self._properties = dict()
        
        for property_type in self.property_types:
            self._properties[property_type] = float()
        
