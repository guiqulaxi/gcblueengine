import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag90kg'
    dbObj.maxRange_m=1624.322876
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=32.289021
    dbObj.fragCharge_kg=27.973986
    dbObj.radCharge_kg=3.228902
    dbObj.fragMetal_kg=29.736994
    dbObj.fragFragment_kg=0.007875
    dbObj.fragSpread=0.300000
    return dbObj
