import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag950kg'
    dbObj.maxRange_m=4472.200195
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=341.830902
    dbObj.fragCharge_kg=294.612732
    dbObj.radCharge_kg=34.183090
    dbObj.fragMetal_kg=313.556366
    dbObj.fragFragment_kg=0.058851
    dbObj.fragSpread=0.300000
    return dbObj
