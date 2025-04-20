import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1600kg'
    dbObj.maxRange_m=5515.385742
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=575.818054
    dbObj.fragCharge_kg=496.121307
    dbObj.radCharge_kg=57.581802
    dbObj.fragMetal_kg=528.060669
    dbObj.fragFragment_kg=0.091677
    dbObj.fragSpread=0.300000
    return dbObj
