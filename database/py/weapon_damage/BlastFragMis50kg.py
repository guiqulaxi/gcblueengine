import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis50kg'
    dbObj.maxRange_m=3431.063232
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=10.175882
    dbObj.fragCharge_kg=22.216078
    dbObj.radCharge_kg=1.017588
    dbObj.fragMetal_kg=17.608040
    dbObj.fragFragment_kg=0.032015
    dbObj.fragSpread=0.300000
    return dbObj
