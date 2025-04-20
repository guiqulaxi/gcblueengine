import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK170'
    dbObj.xSpeed_kts=[0.000000,3.870000,13.545000,19.350000]
    dbObj.ySL_dB=[87.550003,91.810310,121.632500,130.153122]
    dbObj.speedMinNL_kts=9.100000
    dbObj.NL_min=49.200001
    dbObj.speedMaxNL_kts=19.350000
    dbObj.NL_max=94.199997
    dbObj.cavitationOffset_kts=13.000000
    dbObj.cavitationSlope_ktsperft=0.008750
    dbObj.cavitationSL_dB=148.153122
    dbObj.snorkelingSL_dB=142.153122
    dbObj.BuildSLTable()
    return dbObj