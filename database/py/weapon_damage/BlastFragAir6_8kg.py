import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir6.8kg'
    dbObj.maxRange_m=2020.600708
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.718516
    dbObj.fragCharge_kg=2.798323
    dbObj.radCharge_kg=0.171852
    dbObj.fragMetal_kg=2.283161
    dbObj.fragFragment_kg=0.011192
    dbObj.fragSpread=0.080278
    return dbObj
