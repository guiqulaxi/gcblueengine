import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN200'
    dbObj.xSpeed_kts=[0.000000,8.160000,28.559999,40.799999]
    dbObj.ySL_dB=[84.199997,89.197090,124.176720,134.170898]
    dbObj.speedMinNL_kts=9.065000
    dbObj.NL_min=46.700001
    dbObj.speedMaxNL_kts=40.799999
    dbObj.NL_max=90.199997
    dbObj.cavitationOffset_kts=12.950000
    dbObj.cavitationSlope_ktsperft=0.010475
    dbObj.cavitationSL_dB=152.170898
    dbObj.snorkelingSL_dB=146.170898
    dbObj.BuildSLTable()
    return dbObj