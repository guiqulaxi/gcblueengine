import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN145'
    dbObj.xSpeed_kts=[0.000000,5.520000,19.320000,27.600000]
    dbObj.ySL_dB=[104.000000,112.279999,170.240005,186.800003]
    dbObj.speedMinNL_kts=5.600000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=27.600000
    dbObj.NL_max=112.199997
    dbObj.cavitationOffset_kts=8.000000
    dbObj.cavitationSlope_ktsperft=0.003000
    dbObj.cavitationSL_dB=204.800003
    dbObj.snorkelingSL_dB=198.800003
    dbObj.BuildSLTable()
    return dbObj