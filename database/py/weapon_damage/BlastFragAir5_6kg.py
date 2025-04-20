import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir5.6kg'
    dbObj.maxRange_m=1869.761963
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.442064
    dbObj.fragCharge_kg=2.286624
    dbObj.radCharge_kg=0.144206
    dbObj.fragMetal_kg=1.871312
    dbObj.fragFragment_kg=0.009646
    dbObj.fragSpread=0.072600
    return dbObj
