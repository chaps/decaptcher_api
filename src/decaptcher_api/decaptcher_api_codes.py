	
"""
    The response codes as defined in the official API
"""
RESPONSE_CODES = {
    0: {"name": "cc_ERR_OK", "message": "everything went OK"},        
    -1: {"name": "ccERR_GENERAL", "message": "geneeral internal error" },        
    -2: {"name": "ccERR_STATUS", "message": "status is not correct"},        
    -3: {"name": "cERR_NET_ERROR", "message": "network data transfer error"},        
    -4: {"name": "ccERR_TEXT_SIZE", "message": "test is not of an appropriate size"},        
    -5: {"name": "ccERR_OVERLOAD", "message": "server is overloaded"},
    -6: {"name": "ccERR_BALANCE", "message": "not enough funds to complete the request"},        
    -7: {"name": "ccERR_TIMEOUT", "message": "request timed out"}, 
    -8: {"name": "ccERR_BAD_PARAMS", "message": "provided parameters are not good for this function"}, 
    -9: {"name": "ccERR_UNABLE", "message": "unable to recognize the picture"},  
    -200: {"name": "ccERR_UNKNOWN", "message": "unknown error"},
}

RESPONSE_TIMEOUTS = {
    0: {"name":"ptoDEFAULT", "message": "default timeout, server-specific"},
    1: { "name": "ptoLONG", "message":"long timeout for picture, server-specific"},
    2: {"name": "pto30SEC", "message": "30 seconds timeout for picture"},
    3: {"name": "pto60SEC", "message": "60 seconds timeout for picture"},
    4: {"name": "pto90SEC", "message": "90 seconds timeout for picture"},
}

PROCESSING_TYPES = {
    0 : {"name": "ptUNSPECIFIED", "message": "undspecified" },
    82: {"name": "ptMANUAL", "message": "manually processed pictures"},
    83: {"name": "ptASIRRA", "message": "ASIRRA pictures"},
    86: {"name": "ptTEXT", "message": "TEXT questions"},
    87: {"name": "ptMULTIPART", "message": "MULTIPART questions"}
}

#???
PROCESSING_SPECIFICS = {
    12: {"name": "ptASIRRA_PICS_NUM", "message": "asirra pics num"},
    20: {"name": "ptMULTIPRAT_PICS_NUM", "messsage": "multipart pics num"},
}

