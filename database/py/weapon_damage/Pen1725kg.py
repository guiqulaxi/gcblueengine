import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1725kg'
    dbObj.maxRange_m=132.916687
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1207.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=172.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
