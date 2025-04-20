import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S08.Large Cruiser'
    dbObj.xSpeed_kts=[4.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[107.500000,112.120003,125.980003,130.600006]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=54.500000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=94.500000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj