import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.5kg'
    dbObj.maxRange_m=331.719513
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.229103
    dbObj.fragCharge_kg=1.105598
    dbObj.radCharge_kg=0.122910
    dbObj.fragMetal_kg=1.165299
    dbObj.fragFragment_kg=0.000607
    dbObj.fragSpread=0.300000
    return dbObj
