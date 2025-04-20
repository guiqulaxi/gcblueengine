import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir14.5kg'
    dbObj.maxRange_m=2622.666504
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.393687
    dbObj.fragCharge_kg=6.147542
    dbObj.radCharge_kg=0.339369
    dbObj.fragMetal_kg=4.958771
    dbObj.fragFragment_kg=0.018642
    dbObj.fragSpread=0.136489
    return dbObj
