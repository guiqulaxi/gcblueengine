import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK175'
    dbObj.xSpeed_kts=[0.000000,4.240000,14.840000,21.200001]
    dbObj.ySL_dB=[91.400002,96.378342,131.226715,141.183395]
    dbObj.speedMinNL_kts=7.490000
    dbObj.NL_min=49.200001
    dbObj.speedMaxNL_kts=21.200001
    dbObj.NL_max=88.199997
    dbObj.cavitationOffset_kts=10.700000
    dbObj.cavitationSlope_ktsperft=0.004950
    dbObj.cavitationSL_dB=159.183395
    dbObj.snorkelingSL_dB=153.183395
    dbObj.BuildSLTable()
    return dbObj