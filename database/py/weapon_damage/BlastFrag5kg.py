import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag5kg'
    dbObj.maxRange_m=395.256805
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.760306
    dbObj.fragCharge_kg=1.576462
    dbObj.radCharge_kg=0.176031
    dbObj.fragMetal_kg=1.663231
    dbObj.fragFragment_kg=0.000770
    dbObj.fragSpread=0.300000
    return dbObj
