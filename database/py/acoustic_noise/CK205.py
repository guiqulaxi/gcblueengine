import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK205'
    dbObj.xSpeed_kts=[0.000000,5.410000,18.934999,27.049999]
    dbObj.ySL_dB=[86.660004,91.067245,121.917953,130.732437]
    dbObj.speedMinNL_kts=8.505000
    dbObj.NL_min=47.500000
    dbObj.speedMaxNL_kts=27.049999
    dbObj.NL_max=88.500000
    dbObj.cavitationOffset_kts=12.150000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=148.732437
    dbObj.snorkelingSL_dB=142.732437
    dbObj.BuildSLTable()
    return dbObj