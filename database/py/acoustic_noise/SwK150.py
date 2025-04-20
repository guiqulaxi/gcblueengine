import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK150'
    dbObj.xSpeed_kts=[0.000000,3.012000,10.542000,15.060000]
    dbObj.ySL_dB=[93.650002,97.958519,128.118118,136.735153]
    dbObj.speedMinNL_kts=7.945000
    dbObj.NL_min=51.580002
    dbObj.speedMaxNL_kts=15.060000
    dbObj.NL_max=98.949997
    dbObj.cavitationOffset_kts=11.350000
    dbObj.cavitationSlope_ktsperft=0.007680
    dbObj.cavitationSL_dB=154.735153
    dbObj.snorkelingSL_dB=148.735153
    dbObj.BuildSLTable()
    return dbObj