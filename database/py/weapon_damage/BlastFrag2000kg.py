import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2000kg'
    dbObj.maxRange_m=5998.155273
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=719.812561
    dbObj.fragCharge_kg=620.125000
    dbObj.radCharge_kg=71.981255
    dbObj.fragMetal_kg=660.062500
    dbObj.fragFragment_kg=0.109718
    dbObj.fragSpread=0.300000
    return dbObj
