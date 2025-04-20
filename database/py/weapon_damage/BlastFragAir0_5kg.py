import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir0.5kg'
    dbObj.maxRange_m=511.976105
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.150000
    dbObj.fragCharge_kg=0.190000
    dbObj.radCharge_kg=0.015000
    dbObj.fragMetal_kg=0.160000
    dbObj.fragFragment_kg=0.001039
    dbObj.fragSpread=0.045748
    return dbObj
