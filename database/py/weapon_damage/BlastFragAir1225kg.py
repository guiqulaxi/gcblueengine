import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1225kg'
    dbObj.maxRange_m=7294.406738
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=152.670105
    dbObj.fragCharge_kg=608.719910
    dbObj.radCharge_kg=15.267011
    dbObj.fragMetal_kg=463.609955
    dbObj.fragFragment_kg=0.158067
    dbObj.fragSpread=0.300000
    return dbObj
