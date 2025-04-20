import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag22.5kg'
    dbObj.maxRange_m=853.445068
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.023211
    dbObj.fragCharge_kg=7.026193
    dbObj.radCharge_kg=0.802321
    dbObj.fragMetal_kg=7.450596
    dbObj.fragFragment_kg=0.002517
    dbObj.fragSpread=0.300000
    return dbObj
