import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag6.2kg'
    dbObj.maxRange_m=445.910004
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.187001
    dbObj.fragCharge_kg=1.951999
    dbObj.radCharge_kg=0.218700
    dbObj.fragMetal_kg=2.061000
    dbObj.fragFragment_kg=0.000914
    dbObj.fragSpread=0.300000
    return dbObj
