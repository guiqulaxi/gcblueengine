import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN170'
    dbObj.xSpeed_kts=[0.000000,6.720000,23.520000,33.599998]
    dbObj.ySL_dB=[93.500000,101.008652,153.569199,168.586502]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=49.150002
    dbObj.speedMaxNL_kts=33.599998
    dbObj.NL_max=100.949997
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.007450
    dbObj.cavitationSL_dB=186.586502
    dbObj.snorkelingSL_dB=180.586502
    dbObj.BuildSLTable()
    return dbObj