import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK210'
    dbObj.xSpeed_kts=[0.000000,6.008000,21.028000,30.040001]
    dbObj.ySL_dB=[76.480003,79.933838,104.110687,111.018356]
    dbObj.speedMinNL_kts=11.795000
    dbObj.NL_min=43.750000
    dbObj.speedMaxNL_kts=30.040001
    dbObj.NL_max=83.300003
    dbObj.cavitationOffset_kts=16.850000
    dbObj.cavitationSlope_ktsperft=0.015320
    dbObj.cavitationSL_dB=129.018356
    dbObj.snorkelingSL_dB=123.018356
    dbObj.BuildSLTable()
    return dbObj