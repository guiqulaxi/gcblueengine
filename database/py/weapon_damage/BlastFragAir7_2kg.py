import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir7.2kg'
    dbObj.maxRange_m=2067.181152
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.809455
    dbObj.fragCharge_kg=2.969697
    dbObj.radCharge_kg=0.180945
    dbObj.fragMetal_kg=2.420848
    dbObj.fragFragment_kg=0.011695
    dbObj.fragSpread=0.082656
    return dbObj
