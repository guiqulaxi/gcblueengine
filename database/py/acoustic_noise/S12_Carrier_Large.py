import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S12.Carrier Large'
    dbObj.xSpeed_kts=[2.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[112.000000,117.720001,134.880005,140.600006]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=56.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=96.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj