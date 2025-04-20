import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK155'
    dbObj.xSpeed_kts=[0.000000,3.228000,11.298000,16.139999]
    dbObj.ySL_dB=[91.419998,95.698395,125.647133,134.203918]
    dbObj.speedMinNL_kts=8.260000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=16.139999
    dbObj.NL_max=97.800003
    dbObj.cavitationOffset_kts=11.800000
    dbObj.cavitationSlope_ktsperft=0.007100
    dbObj.cavitationSL_dB=152.203918
    dbObj.snorkelingSL_dB=146.203918
    dbObj.BuildSLTable()
    return dbObj