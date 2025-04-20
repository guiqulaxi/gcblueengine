import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK155'
    dbObj.xSpeed_kts=[0.000000,3.280000,11.480000,16.400000]
    dbObj.ySL_dB=[95.800003,100.334274,132.074173,141.142715]
    dbObj.speedMinNL_kts=6.230000
    dbObj.NL_min=51.200001
    dbObj.speedMaxNL_kts=16.400000
    dbObj.NL_max=96.199997
    dbObj.cavitationOffset_kts=8.900000
    dbObj.cavitationSlope_ktsperft=0.003650
    dbObj.cavitationSL_dB=159.142715
    dbObj.snorkelingSL_dB=153.142715
    dbObj.BuildSLTable()
    return dbObj