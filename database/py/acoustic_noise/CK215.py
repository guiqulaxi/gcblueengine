import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK215'
    dbObj.xSpeed_kts=[0.000000,5.870000,20.545000,29.350000]
    dbObj.ySL_dB=[84.419998,88.827019,119.676163,128.490204]
    dbObj.speedMinNL_kts=9.135000
    dbObj.NL_min=46.500000
    dbObj.speedMaxNL_kts=29.350000
    dbObj.NL_max=84.500000
    dbObj.cavitationOffset_kts=13.050000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=146.490204
    dbObj.snorkelingSL_dB=140.490204
    dbObj.BuildSLTable()
    return dbObj