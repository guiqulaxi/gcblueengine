import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis7kg'
    dbObj.maxRange_m=2041.627563
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.764056
    dbObj.fragCharge_kg=2.883963
    dbObj.radCharge_kg=0.176406
    dbObj.fragMetal_kg=2.351981
    dbObj.fragFragment_kg=0.011417
    dbObj.fragSpread=0.081860
    return dbObj
