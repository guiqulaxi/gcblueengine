import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3750kg'
    dbObj.maxRange_m=7692.021973
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1349.796997
    dbObj.fragCharge_kg=1162.635254
    dbObj.radCharge_kg=134.979706
    dbObj.fragMetal_kg=1237.567627
    dbObj.fragFragment_kg=0.188195
    dbObj.fragSpread=0.300000
    return dbObj
