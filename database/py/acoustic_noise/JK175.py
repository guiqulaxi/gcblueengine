import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK175'
    dbObj.xSpeed_kts=[0.000000,4.484000,15.694000,22.420000]
    dbObj.ySL_dB=[87.300003,91.166718,118.233765,125.967201]
    dbObj.speedMinNL_kts=8.960000
    dbObj.NL_min=48.480000
    dbObj.speedMaxNL_kts=22.420000
    dbObj.NL_max=93.000000
    dbObj.cavitationOffset_kts=12.800000
    dbObj.cavitationSlope_ktsperft=0.010720
    dbObj.cavitationSL_dB=143.967194
    dbObj.snorkelingSL_dB=137.967194
    dbObj.BuildSLTable()
    return dbObj