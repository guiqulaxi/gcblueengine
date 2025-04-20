import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast3150kg'
    dbObj.maxRange_m=182.914658
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3150.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=315.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
