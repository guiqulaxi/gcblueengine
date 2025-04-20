import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK215'
    dbObj.xSpeed_kts=[0.000000,5.668000,19.837999,28.340000]
    dbObj.ySL_dB=[76.959999,81.011597,109.372787,117.475990]
    dbObj.speedMinNL_kts=8.960000
    dbObj.NL_min=43.660000
    dbObj.speedMaxNL_kts=28.340000
    dbObj.NL_max=83.680000
    dbObj.cavitationOffset_kts=12.800000
    dbObj.cavitationSlope_ktsperft=0.011860
    dbObj.cavitationSL_dB=135.475983
    dbObj.snorkelingSL_dB=129.475983
    dbObj.BuildSLTable()
    return dbObj