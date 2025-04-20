import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 877E'
    dbObj.xSpeed_kts=[0.000000,5.100000,13.600000,17.000000]
    dbObj.ySL_dB=[91.500000,100.349998,118.000000,127.800003]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=48.500000
    dbObj.speedMaxNL_kts=24.000000
    dbObj.NL_max=98.500000
    dbObj.cavitationOffset_kts=12.000000
    dbObj.cavitationSlope_ktsperft=0.022000
    dbObj.cavitationSL_dB=163.199997
    dbObj.snorkelingSL_dB=139.800003
    dbObj.BuildSLTable()
    return dbObj