import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis23.5kg'
    dbObj.maxRange_m=2979.223633
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.220262
    dbObj.fragCharge_kg=10.149826
    dbObj.radCharge_kg=0.522026
    dbObj.fragMetal_kg=8.129912
    dbObj.fragFragment_kg=0.024053
    dbObj.fragSpread=0.220378
    return dbObj
