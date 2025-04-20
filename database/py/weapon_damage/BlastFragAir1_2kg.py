import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1.2kg'
    dbObj.maxRange_m=868.995667
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.354604
    dbObj.fragCharge_kg=0.459597
    dbObj.radCharge_kg=0.035460
    dbObj.fragMetal_kg=0.385799
    dbObj.fragFragment_kg=0.002426
    dbObj.fragSpread=0.048767
    return dbObj
