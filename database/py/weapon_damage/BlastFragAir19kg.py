import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir19kg'
    dbObj.maxRange_m=2827.353760
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.320243
    dbObj.fragCharge_kg=8.139838
    dbObj.radCharge_kg=0.432024
    dbObj.fragMetal_kg=6.539919
    dbObj.fragFragment_kg=0.021655
    dbObj.fragSpread=0.175934
    return dbObj
