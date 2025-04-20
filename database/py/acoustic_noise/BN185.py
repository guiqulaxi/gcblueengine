import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN185'
    dbObj.xSpeed_kts=[0.000000,7.600000,26.600000,38.000000]
    dbObj.ySL_dB=[86.400002,92.238602,133.108841,144.786041]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=47.240002
    dbObj.speedMaxNL_kts=38.000000
    dbObj.NL_max=93.800003
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.010960
    dbObj.cavitationSL_dB=162.786041
    dbObj.snorkelingSL_dB=156.786041
    dbObj.BuildSLTable()
    return dbObj