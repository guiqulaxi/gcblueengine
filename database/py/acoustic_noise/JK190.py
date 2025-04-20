import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK190'
    dbObj.xSpeed_kts=[0.000000,5.126000,17.941000,25.629999]
    dbObj.ySL_dB=[82.949997,86.621468,112.321716,119.664642]
    dbObj.speedMinNL_kts=9.590000
    dbObj.NL_min=46.619999
    dbObj.speedMaxNL_kts=25.629999
    dbObj.NL_max=89.400002
    dbObj.cavitationOffset_kts=13.700000
    dbObj.cavitationSlope_ktsperft=0.012580
    dbObj.cavitationSL_dB=137.664642
    dbObj.snorkelingSL_dB=131.664642
    dbObj.BuildSLTable()
    return dbObj