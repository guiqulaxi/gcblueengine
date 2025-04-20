import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir6.2kg'
    dbObj.maxRange_m=1948.484497
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.581007
    dbObj.fragCharge_kg=2.541996
    dbObj.radCharge_kg=0.158101
    dbObj.fragMetal_kg=2.076998
    dbObj.fragFragment_kg=0.010437
    dbObj.fragSpread=0.076391
    return dbObj
