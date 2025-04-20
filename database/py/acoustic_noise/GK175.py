import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK175'
    dbObj.xSpeed_kts=[0.000000,4.496000,15.736000,22.480000]
    dbObj.ySL_dB=[83.760002,87.686829,115.174614,123.028267]
    dbObj.speedMinNL_kts=9.590000
    dbObj.NL_min=48.299999
    dbObj.speedMaxNL_kts=22.480000
    dbObj.NL_max=92.400002
    dbObj.cavitationOffset_kts=13.700000
    dbObj.cavitationSlope_ktsperft=0.010840
    dbObj.cavitationSL_dB=141.028259
    dbObj.snorkelingSL_dB=135.028259
    dbObj.BuildSLTable()
    return dbObj