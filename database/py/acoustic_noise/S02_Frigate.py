import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S02.Frigate'
    dbObj.xSpeed_kts=[4.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[106.000000,109.959999,121.839996,125.800003]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=53.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=93.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj