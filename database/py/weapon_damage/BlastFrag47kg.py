import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag47kg'
    dbObj.maxRange_m=1191.189819
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=16.825045
    dbObj.fragCharge_kg=14.633305
    dbObj.radCharge_kg=1.682504
    dbObj.fragMetal_kg=15.541652
    dbObj.fragFragment_kg=0.004476
    dbObj.fragSpread=0.300000
    return dbObj
