import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag335kg'
    dbObj.maxRange_m=2892.846924
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=120.456604
    dbObj.fragCharge_kg=103.945595
    dbObj.radCharge_kg=12.045661
    dbObj.fragMetal_kg=110.597801
    dbObj.fragFragment_kg=0.024085
    dbObj.fragSpread=0.300000
    return dbObj
