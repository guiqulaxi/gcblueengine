import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis80kg'
    dbObj.maxRange_m=3785.766357
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=15.354074
    dbObj.fragCharge_kg=36.163952
    dbObj.radCharge_kg=1.535407
    dbObj.fragMetal_kg=28.481976
    dbObj.fragFragment_kg=0.039177
    dbObj.fragSpread=0.300000
    return dbObj
