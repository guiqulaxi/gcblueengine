import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir185kg'
    dbObj.maxRange_m=4322.450684
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=31.681284
    dbObj.fragCharge_kg=86.179146
    dbObj.radCharge_kg=3.168128
    dbObj.fragMetal_kg=67.139572
    dbObj.fragFragment_kg=0.051566
    dbObj.fragSpread=0.300000
    return dbObj
