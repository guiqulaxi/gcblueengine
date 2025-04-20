import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK170'
    dbObj.xSpeed_kts=[0.000000,3.860000,13.510000,19.299999]
    dbObj.ySL_dB=[88.250000,92.524361,122.444901,130.993622]
    dbObj.speedMinNL_kts=8.925000
    dbObj.NL_min=49.099998
    dbObj.speedMaxNL_kts=19.299999
    dbObj.NL_max=93.949997
    dbObj.cavitationOffset_kts=12.750000
    dbObj.cavitationSlope_ktsperft=0.010400
    dbObj.cavitationSL_dB=148.993622
    dbObj.snorkelingSL_dB=142.993622
    dbObj.BuildSLTable()
    return dbObj