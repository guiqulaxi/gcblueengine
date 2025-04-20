import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK210'
    dbObj.xSpeed_kts=[0.000000,5.640000,19.740000,28.200001]
    dbObj.ySL_dB=[85.540001,89.951965,120.835732,129.659668]
    dbObj.speedMinNL_kts=8.820000
    dbObj.NL_min=47.000000
    dbObj.speedMaxNL_kts=28.200001
    dbObj.NL_max=86.500000
    dbObj.cavitationOffset_kts=12.600000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=147.659668
    dbObj.snorkelingSL_dB=141.659668
    dbObj.BuildSLTable()
    return dbObj