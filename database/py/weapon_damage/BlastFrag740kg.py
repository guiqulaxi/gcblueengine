import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag740kg'
    dbObj.maxRange_m=4043.776855
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=266.237061
    dbObj.fragCharge_kg=229.508621
    dbObj.radCharge_kg=26.623707
    dbObj.fragMetal_kg=244.254318
    dbObj.fragFragment_kg=0.047706
    dbObj.fragSpread=0.300000
    return dbObj
