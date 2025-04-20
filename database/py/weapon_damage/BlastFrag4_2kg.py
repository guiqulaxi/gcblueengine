import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.2kg'
    dbObj.maxRange_m=364.185211
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.476606
    dbObj.fragCharge_kg=1.325596
    dbObj.radCharge_kg=0.147661
    dbObj.fragMetal_kg=1.397798
    dbObj.fragFragment_kg=0.000688
    dbObj.fragSpread=0.300000
    return dbObj
