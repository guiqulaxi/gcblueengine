import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN215'
    dbObj.xSpeed_kts=[0.000000,8.880000,31.080000,44.400002]
    dbObj.ySL_dB=[78.800003,83.201370,114.010948,122.813690]
    dbObj.speedMinNL_kts=10.010000
    dbObj.NL_min=45.200001
    dbObj.speedMaxNL_kts=44.400002
    dbObj.NL_max=84.199997
    dbObj.cavitationOffset_kts=14.300000
    dbObj.cavitationSlope_ktsperft=0.014375
    dbObj.cavitationSL_dB=140.813690
    dbObj.snorkelingSL_dB=134.813690
    dbObj.BuildSLTable()
    return dbObj