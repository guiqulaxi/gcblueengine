import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN150'
    dbObj.xSpeed_kts=[0.000000,5.760000,20.160000,28.799999]
    dbObj.ySL_dB=[98.300003,106.248802,161.890396,177.787994]
    dbObj.speedMinNL_kts=7.980000
    dbObj.NL_min=51.599998
    dbObj.speedMaxNL_kts=28.799999
    dbObj.NL_max=110.000000
    dbObj.cavitationOffset_kts=11.400000
    dbObj.cavitationSlope_ktsperft=0.006550
    dbObj.cavitationSL_dB=195.787994
    dbObj.snorkelingSL_dB=189.787994
    dbObj.BuildSLTable()
    return dbObj