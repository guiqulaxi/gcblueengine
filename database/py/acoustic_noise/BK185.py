import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK185'
    dbObj.xSpeed_kts=[0.000000,4.512000,15.792000,22.559999]
    dbObj.ySL_dB=[84.440002,88.703079,118.544647,127.070816]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=47.240002
    dbObj.speedMaxNL_kts=22.559999
    dbObj.NL_max=90.599998
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.011960
    dbObj.cavitationSL_dB=145.070816
    dbObj.snorkelingSL_dB=139.070816
    dbObj.BuildSLTable()
    return dbObj