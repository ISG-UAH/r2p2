#!/usr/bin/env python

""" This module defines what a naive controller is, from a data-structure POV.

This module contains the definition and implementation of the Naive_Controller
class.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Mario Cobos Maestre"
__authors__ = ["Mario Cobos Maestre"]
__contact__ = "mario.cobos@edu.uah.es"
__copyright__ = "Copyright 2019, UAH"
__credits__ = ["Mario Cobos Maestre"]
__date__ = "2019/03/29"
__deprecated__ = False
__email__ =  "mario.cobos@edu.uah.es"
__license__ = "GPLv3"
__maintainer__ = "Mario Cobos Maestre"
__status__ = "Development"
__version__ = "0.0.1"


import controller

class Naive_Controller(controller.Controller):
    """
        Class implementing an extremely simple naive controller.
        Not really dependable, meant to serve as a simple example
        only.
    """
    def __init__(self):
        """
            Constructor for the Naive_Controller class.
            Outputs:
                - A configured Naive_Controller object.
        """
        super(Naive_Controller, self).__init__("NAIVE")

    def control(self, ang, dst):
        """
            Driver function to centralize and standardize the controller. Can be modified by child classes,
            provided that the result value always is a tuple of the form (angular velocity, acceleration)
        """
        return 0, 3

def create_naive_controller(f):
    """
        Factory for the Naive_Controller class.
        Inputs:
            - f: dictionary. It doesn't get used, it just needs to be included for the sake of standarizing input.
        Outputs:
            - Fully configured Naive_Controller object.
    """
    return Naive_Controller()

controller.register_controller_factory("NAIVE", create_naive_controller)
