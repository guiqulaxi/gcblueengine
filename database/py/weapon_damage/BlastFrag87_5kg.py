import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag87.5kg'
    dbObj.maxRange_m=1603.616943
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=31.389715
    dbObj.fragCharge_kg=27.198523
    dbObj.radCharge_kg=3.138972
    dbObj.fragMetal_kg=28.911762
    dbObj.fragFragment_kg=0.007689
    dbObj.fragSpread=0.300000
    return dbObj
