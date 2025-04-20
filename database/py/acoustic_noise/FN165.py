import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN165'
    dbObj.xSpeed_kts=[0.000000,6.480000,22.680000,32.400002]
    dbObj.ySL_dB=[95.300003,103.127548,157.920410,173.575500]
    dbObj.speedMinNL_kts=7.560000
    dbObj.NL_min=49.759998
    dbObj.speedMaxNL_kts=32.400002
    dbObj.NL_max=103.199997
    dbObj.cavitationOffset_kts=10.800000
    dbObj.cavitationSlope_ktsperft=0.006960
    dbObj.cavitationSL_dB=191.575500
    dbObj.snorkelingSL_dB=185.575500
    dbObj.BuildSLTable()
    return dbObj