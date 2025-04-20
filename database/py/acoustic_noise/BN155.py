import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN155'
    dbObj.xSpeed_kts=[0.000000,6.040000,21.139999,30.200001]
    dbObj.ySL_dB=[96.599998,104.455246,159.441940,175.152420]
    dbObj.speedMinNL_kts=8.120000
    dbObj.NL_min=50.959999
    dbObj.speedMaxNL_kts=30.200001
    dbObj.NL_max=107.599998
    dbObj.cavitationOffset_kts=11.600000
    dbObj.cavitationSlope_ktsperft=0.007240
    dbObj.cavitationSL_dB=193.152420
    dbObj.snorkelingSL_dB=187.152420
    dbObj.BuildSLTable()
    return dbObj