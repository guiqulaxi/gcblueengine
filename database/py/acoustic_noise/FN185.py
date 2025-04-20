import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN185'
    dbObj.xSpeed_kts=[0.000000,7.440000,26.040001,37.200001]
    dbObj.ySL_dB=[88.099998,94.679466,140.735733,153.894669]
    dbObj.speedMinNL_kts=8.120000
    dbObj.NL_min=47.320000
    dbObj.speedMaxNL_kts=37.200001
    dbObj.NL_max=94.199997
    dbObj.cavitationOffset_kts=11.600000
    dbObj.cavitationSlope_ktsperft=0.008920
    dbObj.cavitationSL_dB=171.894669
    dbObj.snorkelingSL_dB=165.894669
    dbObj.BuildSLTable()
    return dbObj