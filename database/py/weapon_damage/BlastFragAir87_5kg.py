import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir87.5kg'
    dbObj.maxRange_m=3818.184082
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=16.600134
    dbObj.fragCharge_kg=39.683243
    dbObj.radCharge_kg=1.660013
    dbObj.fragMetal_kg=31.216621
    dbObj.fragFragment_kg=0.039868
    dbObj.fragSpread=0.300000
    return dbObj
