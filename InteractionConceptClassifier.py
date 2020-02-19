#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file InteractionConceptClassifier.py
 @brief InteractionConceptClassifier
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import InteractiveManage_idl

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import Manage, Manage__POA


# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
interactionconceptclassifier_spec = ["implementation_id", "InteractionConceptClassifier",
		 "type_name",         "InteractionConceptClassifier",
		 "description",       "InteractionConceptClassifier",
		 "version",           "1.0.0",
		 "vendor",            "hiroyasu",
		 "category",          "Category",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class InteractionConceptClassifier
# @brief InteractionConceptClassifier
#
#
class InteractionConceptClassifier(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_textIn = RTC.TimedStringSeq(RTC.Time(0,0),"")
		"""
		"""
		self._textInIn = OpenRTM_aist.InPort("textIn", self._d_textIn)

		"""
		"""
		self._interactivemanagePort = OpenRTM_aist.CorbaPort("interactivemanage")



		"""
		"""
		self._InteractiveManageRequire = OpenRTM_aist.CorbaConsumer(interfaceType=Manage.InteractiveManage)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable

		# Set InPort buffers
		self.addInPort("textIn",self._textInIn)

		# Set OutPort buffers

		# Set service provider to Ports

		# Set service consumers to Ports
		self._interactivemanagePort.registerConsumer("InteractiveManage", "Manage::InteractiveManage", self._InteractiveManageRequire)

		# Set CORBA Service Ports
		self.addPort(self._interactivemanagePort)

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK

	##
	#
	# The deactivated action (Active state exit action)
	# former rtc_active_exit()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
                while self._textInIn.isNew():
                        ut = time.time()
                        print (int(ut*100000))
                        i = 0
                        indata = self._textInIn.read()
                        try :
                                if "に" in indata.data:
                                        i = indata.data.index("に")
                                        indata.data[i-1] = "2"
                        except:
                                print("NoCategory")

                        try :
                                if "から" in indata.data:
                                        i = indata.data.index("から")
                                        indata.data[i-1] = "2"
                        except:
                                print("NoCategory")

                        try :
                                if "で" in indata.data:
                                        i = indata.data.index("で")
                                        indata.data[i-1] = "2"
                        except:
                                print("NoCategory")

                        try :
                                if "へ" in indata.data:
                                        i = indata.data.index("へ")
                                        indata.data[i-1] = "2"
                        except:
                                print("NoCategory")

                        try :
                                if "まで" in indata.data:
                                        i = indata.data.index("まで")
                                        indata.data[i-1] = "2"
                        except:
                                print("NoCategory")

                        try :
                                if "より" in indata.data:
                                        i = indata.data.index("より")
                                        indata.data[i-1] = "2"
                        except:
                                print("NoCategory")
                        
                        try :
                                if "を" in indata.data:
                                        i = indata.data.index("を")
                                        indata.data[i-1] = "1"
                        except:
                                print("NoCategory")
                        try :
                                if "と" in indata.data:
                                        i = indata.data.index("と")
                                        indata.data[i-1] = "1"
                        except:
                                print("NoCategory")

                        try :
                                if "の" in indata.data:
                                        i = indata.data.index("の")
                                        indata.data[i-1] = indata.data[i+1]
                        except:
                                print("NoCategory")

                        systemid = "goods"
                        speechid = indata.data
                        print (systemid)
                        print str(speechid).decode('string-escape')
                        ut1 = time.time()
                        print (int(ut1*100000))
                        self._InteractiveManageRequire._ptr().read(systemid,speechid)	
		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def InteractionConceptClassifierInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=interactionconceptclassifier_spec)
    manager.registerFactory(profile,
                            InteractionConceptClassifier,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    InteractionConceptClassifierInit(manager)

    # Create a component
    comp = manager.createComponent("InteractionConceptClassifier")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

