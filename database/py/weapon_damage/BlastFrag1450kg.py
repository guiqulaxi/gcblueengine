import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1450kg'
    dbObj.maxRange_m=5308.027832
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=521.820496
    dbObj.fragCharge_kg=449.619690
    dbObj.radCharge_kg=52.182049
    dbObj.fragMetal_kg=478.559845
    dbObj.fragFragment_kg=0.084491
    dbObj.fragSpread=0.300000
    return dbObj
