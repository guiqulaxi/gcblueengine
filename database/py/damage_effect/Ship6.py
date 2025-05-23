# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Ship6'
    dbObj.blastEffect=[pygcb.DamagePoint()]*5
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.500000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=7.000000
    dbObj.blastEffect[2].damageFactor=0.000000
    dbObj.blastEffect[3].effectLevel=15.000000
    dbObj.blastEffect[3].damageFactor=2.000000
    dbObj.blastEffect[4].effectLevel=60.000000
    dbObj.blastEffect[4].damageFactor=20.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*5
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=300.000000
    dbObj.waterBlastEffect[1].damageFactor=0.000000
    dbObj.waterBlastEffect[2].effectLevel=600.000000
    dbObj.waterBlastEffect[2].damageFactor=0.100000
    dbObj.waterBlastEffect[3].effectLevel=2000.000000
    dbObj.waterBlastEffect[3].damageFactor=0.150000
    dbObj.waterBlastEffect[4].effectLevel=20000.000000
    dbObj.waterBlastEffect[4].damageFactor=2.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*7
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=5000.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=75000.000000
    dbObj.fragEffect[2].damageFactor=0.010000
    dbObj.fragEffect[3].effectLevel=25000000.000000
    dbObj.fragEffect[3].damageFactor=0.050000
    dbObj.fragEffect[4].effectLevel=50000000.000000
    dbObj.fragEffect[4].damageFactor=0.200000
    dbObj.fragEffect[5].effectLevel=150000000.000000
    dbObj.fragEffect[5].damageFactor=0.700000
    dbObj.fragEffect[6].effectLevel=700000000.000000
    dbObj.fragEffect[6].damageFactor=2.000000
    dbObj.radEffect=[pygcb.DamagePoint()]*6
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=5000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=25000.000000
    dbObj.radEffect[2].damageFactor=0.400000
    dbObj.radEffect[3].effectLevel=50000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=125000.000000
    dbObj.radEffect[4].damageFactor=5.000000
    dbObj.radEffect[5].effectLevel=250000.000000
    dbObj.radEffect[5].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*7
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.000000
    dbObj.internalEffect[2].effectLevel=125.000000
    dbObj.internalEffect[2].damageFactor=0.200000
    dbObj.internalEffect[3].effectLevel=250.000000
    dbObj.internalEffect[3].damageFactor=1.000000
    dbObj.internalEffect[4].effectLevel=500.000000
    dbObj.internalEffect[4].damageFactor=2.000000
    dbObj.internalEffect[5].effectLevel=1250.000000
    dbObj.internalEffect[5].damageFactor=5.000000
    dbObj.internalEffect[6].effectLevel=2500.000000
    dbObj.internalEffect[6].damageFactor=20.000000
    return dbObj
