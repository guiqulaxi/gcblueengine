import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK175'
    dbObj.xSpeed_kts=[0.000000,3.972000,13.902000,19.860001]
    dbObj.ySL_dB=[87.959999,92.275757,122.486053,131.117569]
    dbObj.speedMinNL_kts=8.708000
    dbObj.NL_min=48.540001
    dbObj.speedMaxNL_kts=19.860001
    dbObj.NL_max=92.940002
    dbObj.cavitationOffset_kts=12.440000
    dbObj.cavitationSlope_ktsperft=0.008420
    dbObj.cavitationSL_dB=149.117569
    dbObj.snorkelingSL_dB=143.117569
    dbObj.BuildSLTable()
    return dbObj