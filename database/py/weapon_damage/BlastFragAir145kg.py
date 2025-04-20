import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir145kg'
    dbObj.maxRange_m=4154.802246
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=25.702503
    dbObj.fragCharge_kg=66.964996
    dbObj.radCharge_kg=2.570250
    dbObj.fragMetal_kg=52.332500
    dbObj.fragFragment_kg=0.047489
    dbObj.fragSpread=0.300000
    return dbObj
