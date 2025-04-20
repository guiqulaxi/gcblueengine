import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3kg'
    dbObj.maxRange_m=1407.635010
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.818715
    dbObj.fragCharge_kg=1.194190
    dbObj.radCharge_kg=0.081871
    dbObj.fragMetal_kg=0.987095
    dbObj.fragFragment_kg=0.005673
    dbObj.fragSpread=0.058403
    return dbObj
