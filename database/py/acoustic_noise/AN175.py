import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN175'
    dbObj.xSpeed_kts=[0.000000,6.960000,24.360001,34.799999]
    dbObj.ySL_dB=[89.800003,96.130348,140.442764,153.103455]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=48.599998
    dbObj.speedMaxNL_kts=34.799999
    dbObj.NL_max=99.000000
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.009300
    dbObj.cavitationSL_dB=171.103455
    dbObj.snorkelingSL_dB=165.103455
    dbObj.BuildSLTable()
    return dbObj