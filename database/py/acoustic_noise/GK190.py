import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK190'
    dbObj.xSpeed_kts=[0.000000,5.144000,18.004000,25.719999]
    dbObj.ySL_dB=[80.639999,84.395508,110.684090,118.195114]
    dbObj.speedMinNL_kts=10.535000
    dbObj.NL_min=46.349998
    dbObj.speedMaxNL_kts=25.719999
    dbObj.NL_max=88.500000
    dbObj.cavitationOffset_kts=15.050000
    dbObj.cavitationSlope_ktsperft=0.012760
    dbObj.cavitationSL_dB=136.195114
    dbObj.snorkelingSL_dB=130.195114
    dbObj.BuildSLTable()
    return dbObj