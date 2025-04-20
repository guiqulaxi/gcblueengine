import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK190'
    dbObj.xSpeed_kts=[0.000000,4.608000,16.128000,23.040001]
    dbObj.ySL_dB=[83.760002,88.200729,119.285851,128.167313]
    dbObj.speedMinNL_kts=8.260000
    dbObj.NL_min=46.709999
    dbObj.speedMaxNL_kts=23.040001
    dbObj.NL_max=89.580002
    dbObj.cavitationOffset_kts=11.800000
    dbObj.cavitationSlope_ktsperft=0.009410
    dbObj.cavitationSL_dB=146.167313
    dbObj.snorkelingSL_dB=140.167313
    dbObj.BuildSLTable()
    return dbObj