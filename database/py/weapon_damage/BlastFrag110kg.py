import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag110kg'
    dbObj.maxRange_m=1783.437378
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=39.484074
    dbObj.fragCharge_kg=34.177284
    dbObj.radCharge_kg=3.948407
    dbObj.fragMetal_kg=36.338642
    dbObj.fragFragment_kg=0.009385
    dbObj.fragSpread=0.300000
    return dbObj
