import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK180'
    dbObj.xSpeed_kts=[0.000000,4.184000,14.644000,20.920000]
    dbObj.ySL_dB=[86.480003,91.023933,122.831467,131.919327]
    dbObj.speedMinNL_kts=7.980000
    dbObj.NL_min=47.930000
    dbObj.speedMaxNL_kts=20.920000
    dbObj.NL_max=91.940002
    dbObj.cavitationOffset_kts=11.400000
    dbObj.cavitationSlope_ktsperft=0.008430
    dbObj.cavitationSL_dB=149.919327
    dbObj.snorkelingSL_dB=143.919327
    dbObj.BuildSLTable()
    return dbObj