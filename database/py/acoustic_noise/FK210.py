import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK210'
    dbObj.xSpeed_kts=[0.000000,5.456000,19.096001,27.280001]
    dbObj.ySL_dB=[78.320000,82.460190,111.441505,119.721878]
    dbObj.speedMinNL_kts=8.820000
    dbObj.NL_min=44.270000
    dbObj.speedMaxNL_kts=27.280001
    dbObj.NL_max=84.860001
    dbObj.cavitationOffset_kts=12.600000
    dbObj.cavitationSlope_ktsperft=0.011370
    dbObj.cavitationSL_dB=137.721878
    dbObj.snorkelingSL_dB=131.721878
    dbObj.BuildSLTable()
    return dbObj