import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag375kg'
    dbObj.maxRange_m=3018.227051
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=134.853821
    dbObj.fragCharge_kg=116.347450
    dbObj.radCharge_kg=13.485382
    dbObj.fragMetal_kg=123.798729
    dbObj.fragFragment_kg=0.026229
    dbObj.fragSpread=0.300000
    return dbObj
