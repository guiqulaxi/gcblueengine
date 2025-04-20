import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag37kg'
    dbObj.maxRange_m=1068.361450
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=13.230944
    dbObj.fragCharge_kg=11.529371
    dbObj.radCharge_kg=1.323094
    dbObj.fragMetal_kg=12.239685
    dbObj.fragFragment_kg=0.003696
    dbObj.fragSpread=0.300000
    return dbObj
