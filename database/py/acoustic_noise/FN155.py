import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN155'
    dbObj.xSpeed_kts=[0.000000,6.000000,21.000000,30.000000]
    dbObj.ySL_dB=[98.900002,107.370689,166.665497,183.606873]
    dbObj.speedMinNL_kts=7.280000
    dbObj.NL_min=50.980000
    dbObj.speedMaxNL_kts=30.000000
    dbObj.NL_max=107.699997
    dbObj.cavitationOffset_kts=10.400000
    dbObj.cavitationSlope_ktsperft=0.005980
    dbObj.cavitationSL_dB=201.606873
    dbObj.snorkelingSL_dB=195.606873
    dbObj.BuildSLTable()
    return dbObj