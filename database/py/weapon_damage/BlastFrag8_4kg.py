import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag8.4kg'
    dbObj.maxRange_m=520.486450
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.971511
    dbObj.fragCharge_kg=2.638993
    dbObj.radCharge_kg=0.297151
    dbObj.fragMetal_kg=2.789496
    dbObj.fragFragment_kg=0.001147
    dbObj.fragSpread=0.300000
    return dbObj
