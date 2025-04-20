import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK165'
    dbObj.xSpeed_kts=[0.000000,4.056000,14.196000,20.280001]
    dbObj.ySL_dB=[90.199997,94.158394,121.867180,129.783966]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=49.720001
    dbObj.speedMaxNL_kts=20.280001
    dbObj.NL_max=95.400002
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.009480
    dbObj.cavitationSL_dB=147.783966
    dbObj.snorkelingSL_dB=141.783966
    dbObj.BuildSLTable()
    return dbObj