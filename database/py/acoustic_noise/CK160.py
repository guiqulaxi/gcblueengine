import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK160'
    dbObj.xSpeed_kts=[0.000000,3.340000,11.690000,16.700001]
    dbObj.ySL_dB=[96.739998,101.917000,138.156006,148.509995]
    dbObj.speedMinNL_kts=5.670000
    dbObj.NL_min=52.000000
    dbObj.speedMaxNL_kts=16.700001
    dbObj.NL_max=106.500000
    dbObj.cavitationOffset_kts=8.100000
    dbObj.cavitationSlope_ktsperft=0.003000
    dbObj.cavitationSL_dB=166.509995
    dbObj.snorkelingSL_dB=160.509995
    dbObj.BuildSLTable()
    return dbObj