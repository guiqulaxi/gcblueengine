import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN170'
    dbObj.xSpeed_kts=[0.000000,5.520000,19.320000,27.600000]
    dbObj.ySL_dB=[97.000000,105.593605,165.748840,182.936050]
    dbObj.speedMinNL_kts=6.300000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=27.600000
    dbObj.NL_max=102.500000
    dbObj.cavitationOffset_kts=9.000000
    dbObj.cavitationSlope_ktsperft=0.004000
    dbObj.cavitationSL_dB=200.936050
    dbObj.snorkelingSL_dB=194.936050
    dbObj.BuildSLTable()
    return dbObj