import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN195'
    dbObj.xSpeed_kts=[0.000000,6.670000,23.344999,33.349998]
    dbObj.ySL_dB=[87.750000,93.591789,134.484314,146.167892]
    dbObj.speedMinNL_kts=7.875000
    dbObj.NL_min=48.500000
    dbObj.speedMaxNL_kts=33.349998
    dbObj.NL_max=92.500000
    dbObj.cavitationOffset_kts=11.250000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=164.167892
    dbObj.snorkelingSL_dB=158.167892
    dbObj.BuildSLTable()
    return dbObj