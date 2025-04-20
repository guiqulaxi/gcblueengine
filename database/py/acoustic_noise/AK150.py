import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK150'
    dbObj.xSpeed_kts=[0.000000,3.014000,10.549000,15.070000]
    dbObj.ySL_dB=[92.709999,96.959740,126.707916,135.207397]
    dbObj.speedMinNL_kts=7.980000
    dbObj.NL_min=51.599998
    dbObj.speedMaxNL_kts=15.070000
    dbObj.NL_max=99.000000
    dbObj.cavitationOffset_kts=11.400000
    dbObj.cavitationSlope_ktsperft=0.006550
    dbObj.cavitationSL_dB=153.207397
    dbObj.snorkelingSL_dB=147.207397
    dbObj.BuildSLTable()
    return dbObj