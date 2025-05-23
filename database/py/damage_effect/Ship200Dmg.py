# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Ship200Dmg'
    dbObj.blastEffect=[pygcb.DamagePoint()]*8
    dbObj.blastEffect[0].effectLevel=1.500000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.500000
    dbObj.blastEffect[1].damageFactor=0.200000
    dbObj.blastEffect[2].effectLevel=7.000000
    dbObj.blastEffect[2].damageFactor=1.000000
    dbObj.blastEffect[3].effectLevel=8.800000
    dbObj.blastEffect[3].damageFactor=2.000000
    dbObj.blastEffect[4].effectLevel=8.800000
    dbObj.blastEffect[4].damageFactor=2.000000
    dbObj.blastEffect[5].effectLevel=11.100000
    dbObj.blastEffect[5].damageFactor=4.000000
    dbObj.blastEffect[6].effectLevel=14.000000
    dbObj.blastEffect[6].damageFactor=8.000000
    dbObj.blastEffect[7].effectLevel=17.600000
    dbObj.blastEffect[7].damageFactor=16.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*5
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=40.000000
    dbObj.waterBlastEffect[1].damageFactor=0.000000
    dbObj.waterBlastEffect[2].effectLevel=350.000000
    dbObj.waterBlastEffect[2].damageFactor=0.450000
    dbObj.waterBlastEffect[3].effectLevel=1750.000000
    dbObj.waterBlastEffect[3].damageFactor=0.900000
    dbObj.waterBlastEffect[4].effectLevel=17500.000000
    dbObj.waterBlastEffect[4].damageFactor=1.800000
    dbObj.fragEffect=[pygcb.DamagePoint()]*14
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=7000.000000
    dbObj.fragEffect[1].damageFactor=0.025700
    dbObj.fragEffect[2].effectLevel=11500.000000
    dbObj.fragEffect[2].damageFactor=0.041900
    dbObj.fragEffect[3].effectLevel=33300.000000
    dbObj.fragEffect[3].damageFactor=0.064900
    dbObj.fragEffect[4].effectLevel=60400.000000
    dbObj.fragEffect[4].damageFactor=0.095700
    dbObj.fragEffect[5].effectLevel=2660000.000000
    dbObj.fragEffect[5].damageFactor=0.234000
    dbObj.fragEffect[6].effectLevel=5800000.000000
    dbObj.fragEffect[6].damageFactor=0.304000
    dbObj.fragEffect[7].effectLevel=7550000.000000
    dbObj.fragEffect[7].damageFactor=0.345000
    dbObj.fragEffect[8].effectLevel=8000000.000000
    dbObj.fragEffect[8].damageFactor=0.362000
    dbObj.fragEffect[9].effectLevel=10000000.000000
    dbObj.fragEffect[9].damageFactor=0.383000
    dbObj.fragEffect[10].effectLevel=15000000.000000
    dbObj.fragEffect[10].damageFactor=0.391000
    dbObj.fragEffect[11].effectLevel=25000000.000000
    dbObj.fragEffect[11].damageFactor=0.449000
    dbObj.fragEffect[12].effectLevel=300000000.000000
    dbObj.fragEffect[12].damageFactor=1.170000
    dbObj.fragEffect[13].effectLevel=3000000000.000000
    dbObj.fragEffect[13].damageFactor=1.560000
    dbObj.radEffect=[pygcb.DamagePoint()]*5
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=3000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=11750.000000
    dbObj.radEffect[2].damageFactor=0.000000
    dbObj.radEffect[3].effectLevel=23500.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=70000.000000
    dbObj.radEffect[4].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*16
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=0.500000
    dbObj.internalEffect[1].damageFactor=0.031100
    dbObj.internalEffect[2].effectLevel=1.000000
    dbObj.internalEffect[2].damageFactor=0.062100
    dbObj.internalEffect[3].effectLevel=2.000000
    dbObj.internalEffect[3].damageFactor=0.124000
    dbObj.internalEffect[4].effectLevel=4.000000
    dbObj.internalEffect[4].damageFactor=0.248000
    dbObj.internalEffect[5].effectLevel=8.000000
    dbObj.internalEffect[5].damageFactor=0.496000
    dbObj.internalEffect[6].effectLevel=16.000000
    dbObj.internalEffect[6].damageFactor=0.990000
    dbObj.internalEffect[7].effectLevel=32.000000
    dbObj.internalEffect[7].damageFactor=1.980000
    dbObj.internalEffect[8].effectLevel=64.000000
    dbObj.internalEffect[8].damageFactor=3.960000
    dbObj.internalEffect[9].effectLevel=128.000000
    dbObj.internalEffect[9].damageFactor=7.900000
    dbObj.internalEffect[10].effectLevel=256.000000
    dbObj.internalEffect[10].damageFactor=15.800000
    dbObj.internalEffect[11].effectLevel=512.000000
    dbObj.internalEffect[11].damageFactor=31.600000
    dbObj.internalEffect[12].effectLevel=1024.000000
    dbObj.internalEffect[12].damageFactor=63.099998
    dbObj.internalEffect[13].effectLevel=2048.000000
    dbObj.internalEffect[13].damageFactor=126.000000
    dbObj.internalEffect[14].effectLevel=4096.000000
    dbObj.internalEffect[14].damageFactor=252.000000
    dbObj.internalEffect[15].effectLevel=8192.000000
    dbObj.internalEffect[15].damageFactor=504.000000
    return dbObj
