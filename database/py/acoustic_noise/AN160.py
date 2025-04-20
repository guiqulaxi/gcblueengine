import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN160'
    dbObj.xSpeed_kts=[0.000000,6.240000,21.840000,31.200001]
    dbObj.ySL_dB=[94.900002,102.188522,153.208160,167.785202]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=50.400002
    dbObj.speedMaxNL_kts=31.200001
    dbObj.NL_max=105.599998
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.007650
    dbObj.cavitationSL_dB=185.785202
    dbObj.snorkelingSL_dB=179.785202
    dbObj.BuildSLTable()
    return dbObj