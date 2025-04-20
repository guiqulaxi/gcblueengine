import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK195'
    dbObj.xSpeed_kts=[0.000000,4.950000,17.325001,24.750000]
    dbObj.ySL_dB=[88.900002,93.265480,123.823845,132.554810]
    dbObj.speedMinNL_kts=7.875000
    dbObj.NL_min=48.500000
    dbObj.speedMaxNL_kts=24.750000
    dbObj.NL_max=92.500000
    dbObj.cavitationOffset_kts=11.250000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=150.554810
    dbObj.snorkelingSL_dB=144.554810
    dbObj.BuildSLTable()
    return dbObj