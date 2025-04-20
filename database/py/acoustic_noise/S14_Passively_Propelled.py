import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S14.Passively Propelled'
    dbObj.xSpeed_kts=[0.000000,9.000000,18.000000,36.000000]
    dbObj.ySL_dB=[100.000000,101.760002,107.040001,108.800003]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=50.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=70.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj