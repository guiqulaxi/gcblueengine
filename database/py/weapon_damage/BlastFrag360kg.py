import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag360kg'
    dbObj.maxRange_m=2972.703369
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=129.454834
    dbObj.fragCharge_kg=111.696777
    dbObj.radCharge_kg=12.945483
    dbObj.fragMetal_kg=118.848389
    dbObj.fragFragment_kg=0.025438
    dbObj.fragSpread=0.300000
    return dbObj
