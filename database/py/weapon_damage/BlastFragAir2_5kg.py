import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2.5kg'
    dbObj.maxRange_m=1286.533203
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.693504
    dbObj.fragCharge_kg=0.987664
    dbObj.radCharge_kg=0.069350
    dbObj.fragMetal_kg=0.818832
    dbObj.fragFragment_kg=0.004817
    dbObj.fragSpread=0.055748
    return dbObj
