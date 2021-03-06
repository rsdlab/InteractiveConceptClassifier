﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file InteractiveManage_idl_example.py
 @brief Python example implementations generated from InteractiveManage.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import Manage, Manage__POA



class InteractiveManage_i (Manage__POA.InteractiveManage):
    """
    @class InteractiveManage_i
    Example class implementing IDL interface Manage.InteractiveManage
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # void read(in string systemid, in StringList speechid)
    def read(self, systemid, speechid):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = InteractiveManage_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print(orb.object_to_string(objref))

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

