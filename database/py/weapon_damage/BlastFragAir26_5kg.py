import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir26.5kg'
    dbObj.maxRange_m=3060.757324
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.808155
    dbObj.fragCharge_kg=11.497896
    dbObj.radCharge_kg=0.580815
    dbObj.fragMetal_kg=9.193949
    dbObj.fragFragment_kg=0.025398
    dbObj.fragSpread=0.252786
    return dbObj
