import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast21.5kg'
    dbObj.maxRange_m=34.754662
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=21.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.150000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
