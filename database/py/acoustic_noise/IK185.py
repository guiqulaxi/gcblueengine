import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK185'
    dbObj.xSpeed_kts=[0.000000,4.396000,15.386000,21.980000]
    dbObj.ySL_dB=[85.279999,89.500473,119.043777,127.484726]
    dbObj.speedMinNL_kts=9.044000
    dbObj.NL_min=47.320000
    dbObj.speedMaxNL_kts=21.980000
    dbObj.NL_max=90.519997
    dbObj.cavitationOffset_kts=12.920000
    dbObj.cavitationSlope_ktsperft=0.009560
    dbObj.cavitationSL_dB=145.484726
    dbObj.snorkelingSL_dB=139.484726
    dbObj.BuildSLTable()
    return dbObj