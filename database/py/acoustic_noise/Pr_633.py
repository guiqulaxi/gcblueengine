import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 633'
    dbObj.xSpeed_kts=[0.000000,3.900000,10.400000,13.000000]
    dbObj.ySL_dB=[98.800003,118.360001,161.000000,173.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=55.500000
    dbObj.speedMaxNL_kts=16.000000
    dbObj.NL_max=106.000000
    dbObj.cavitationOffset_kts=8.550000
    dbObj.cavitationSlope_ktsperft=0.015000
    dbObj.cavitationSL_dB=178.199997
    dbObj.snorkelingSL_dB=185.000000
    dbObj.BuildSLTable()
    return dbObj