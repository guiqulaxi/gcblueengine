import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN170'
    dbObj.xSpeed_kts=[0.000000,6.720000,23.520000,33.599998]
    dbObj.ySL_dB=[95.000000,103.218956,160.751648,177.189575]
    dbObj.speedMinNL_kts=7.175000
    dbObj.NL_min=49.700001
    dbObj.speedMaxNL_kts=33.599998
    dbObj.NL_max=102.199997
    dbObj.cavitationOffset_kts=10.250000
    dbObj.cavitationSlope_ktsperft=0.004625
    dbObj.cavitationSL_dB=195.189575
    dbObj.snorkelingSL_dB=189.189575
    dbObj.BuildSLTable()
    return dbObj