import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK180'
    dbObj.xSpeed_kts=[0.000000,4.184000,14.644000,20.920000]
    dbObj.ySL_dB=[86.620003,90.893341,120.806702,129.353378]
    dbObj.speedMinNL_kts=8.876000
    dbObj.NL_min=47.930000
    dbObj.speedMaxNL_kts=20.920000
    dbObj.NL_max=91.730003
    dbObj.cavitationOffset_kts=12.680000
    dbObj.cavitationSlope_ktsperft=0.008990
    dbObj.cavitationSL_dB=147.353378
    dbObj.snorkelingSL_dB=141.353378
    dbObj.BuildSLTable()
    return dbObj