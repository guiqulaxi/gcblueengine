import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1650kg'
    dbObj.maxRange_m=8243.232422
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=193.517212
    dbObj.fragCharge_kg=827.988525
    dbObj.radCharge_kg=19.351721
    dbObj.fragMetal_kg=628.494263
    dbObj.fragFragment_kg=0.206810
    dbObj.fragSpread=0.300000
    return dbObj
