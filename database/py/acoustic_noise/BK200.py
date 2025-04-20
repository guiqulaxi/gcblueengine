import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK200'
    dbObj.xSpeed_kts=[0.000000,5.154000,18.039000,25.770000]
    dbObj.ySL_dB=[80.480003,84.524666,112.837318,120.926643]
    dbObj.speedMinNL_kts=10.010000
    dbObj.NL_min=45.380001
    dbObj.speedMaxNL_kts=25.770000
    dbObj.NL_max=87.000000
    dbObj.cavitationOffset_kts=14.300000
    dbObj.cavitationSlope_ktsperft=0.013820
    dbObj.cavitationSL_dB=138.926651
    dbObj.snorkelingSL_dB=132.926651
    dbObj.BuildSLTable()
    return dbObj