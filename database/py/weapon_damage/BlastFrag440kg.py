import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag440kg'
    dbObj.maxRange_m=3228.825195
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=158.249878
    dbObj.fragCharge_kg=136.500076
    dbObj.radCharge_kg=15.824988
    dbObj.fragMetal_kg=145.250046
    dbObj.fragFragment_kg=0.030060
    dbObj.fragSpread=0.300000
    return dbObj
