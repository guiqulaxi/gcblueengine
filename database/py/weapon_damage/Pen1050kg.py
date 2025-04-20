import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1050kg'
    dbObj.maxRange_m=112.663902
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=735.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=105.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
