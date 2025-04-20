import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK155'
    dbObj.xSpeed_kts=[0.000000,3.632000,12.712000,18.160000]
    dbObj.ySL_dB=[87.919998,91.948631,120.149063,128.206329]
    dbObj.speedMinNL_kts=8.330000
    dbObj.NL_min=50.900002
    dbObj.speedMaxNL_kts=18.160000
    dbObj.NL_max=97.599998
    dbObj.cavitationOffset_kts=11.900000
    dbObj.cavitationSlope_ktsperft=0.008280
    dbObj.cavitationSL_dB=146.206329
    dbObj.snorkelingSL_dB=140.206329
    dbObj.BuildSLTable()
    return dbObj