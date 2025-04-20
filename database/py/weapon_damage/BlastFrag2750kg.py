import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2750kg'
    dbObj.maxRange_m=6826.455566
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=989.804688
    dbObj.fragCharge_kg=852.630188
    dbObj.radCharge_kg=98.980469
    dbObj.fragMetal_kg=907.565125
    dbObj.fragFragment_kg=0.145071
    dbObj.fragSpread=0.300000
    return dbObj
