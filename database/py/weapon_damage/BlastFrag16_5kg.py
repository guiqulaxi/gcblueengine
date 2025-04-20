import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag16.5kg'
    dbObj.maxRange_m=736.863342
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.870861
    dbObj.fragCharge_kg=5.161093
    dbObj.radCharge_kg=0.587086
    dbObj.fragMetal_kg=5.468047
    dbObj.fragFragment_kg=0.001975
    dbObj.fragSpread=0.300000
    return dbObj
