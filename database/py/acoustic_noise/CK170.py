import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK170'
    dbObj.xSpeed_kts=[0.000000,3.800000,13.300000,19.000000]
    dbObj.ySL_dB=[94.500000,99.928223,137.925797,148.782242]
    dbObj.speedMinNL_kts=6.300000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=19.000000
    dbObj.NL_max=102.500000
    dbObj.cavitationOffset_kts=9.000000
    dbObj.cavitationSlope_ktsperft=0.004000
    dbObj.cavitationSL_dB=166.782242
    dbObj.snorkelingSL_dB=160.782242
    dbObj.BuildSLTable()
    return dbObj