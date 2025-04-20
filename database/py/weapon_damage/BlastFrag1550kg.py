import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1550kg'
    dbObj.maxRange_m=5448.097168
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=557.818848
    dbObj.fragCharge_kg=480.620789
    dbObj.radCharge_kg=55.781883
    dbObj.fragMetal_kg=511.560394
    dbObj.fragFragment_kg=0.089309
    dbObj.fragSpread=0.300000
    return dbObj
