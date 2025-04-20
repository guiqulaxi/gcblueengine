import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Default'
    dbObj.xSpeed_kts=[0.000000,5.000000,20.000000,30.000000]
    dbObj.ySL_dB=[100.000000,100.000000,120.000000,140.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=70.000000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=6.000000
    dbObj.cavitationSlope_ktsperft=0.560000
    dbObj.cavitationSL_dB=150.000000
    dbObj.snorkelingSL_dB=150.000000
    dbObj.BuildSLTable()
    return dbObj