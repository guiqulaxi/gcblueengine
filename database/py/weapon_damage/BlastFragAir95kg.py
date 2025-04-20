import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir95kg'
    dbObj.maxRange_m=3846.333740
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=17.830320
    dbObj.fragCharge_kg=43.213120
    dbObj.radCharge_kg=1.783032
    dbObj.fragMetal_kg=33.956558
    dbObj.fragFragment_kg=0.040473
    dbObj.fragSpread=0.300000
    return dbObj
