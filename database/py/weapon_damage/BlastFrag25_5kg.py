import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag25.5kg'
    dbObj.maxRange_m=901.911438
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.100124
    dbObj.fragCharge_kg=7.958251
    dbObj.radCharge_kg=0.910012
    dbObj.fragMetal_kg=8.441626
    dbObj.fragFragment_kg=0.002762
    dbObj.fragSpread=0.300000
    return dbObj
