import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag39kg'
    dbObj.maxRange_m=1094.921997
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=13.949645
    dbObj.fragCharge_kg=12.150236
    dbObj.radCharge_kg=1.394965
    dbObj.fragMetal_kg=12.900118
    dbObj.fragFragment_kg=0.003858
    dbObj.fragSpread=0.300000
    return dbObj
