import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK200'
    dbObj.xSpeed_kts=[0.000000,5.440000,19.040001,27.200001]
    dbObj.ySL_dB=[85.900002,89.130905,111.747261,118.209076]
    dbObj.speedMinNL_kts=9.065000
    dbObj.NL_min=46.700001
    dbObj.speedMaxNL_kts=27.200001
    dbObj.NL_max=78.199997
    dbObj.cavitationOffset_kts=12.950000
    dbObj.cavitationSlope_ktsperft=0.010475
    dbObj.cavitationSL_dB=136.209076
    dbObj.snorkelingSL_dB=130.209076
    dbObj.BuildSLTable()
    return dbObj