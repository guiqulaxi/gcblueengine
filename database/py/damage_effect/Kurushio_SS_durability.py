# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Kurushio SS durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.560000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.690000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.080000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=3.740000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=4.650000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=5.830000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=7.270000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=8.970000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=10.930000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=13.150000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=15.630000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=19.690001
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*13
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=52.861000
    dbObj.waterBlastEffect[1].damageFactor=0.100000
    dbObj.waterBlastEffect[2].effectLevel=83.362000
    dbObj.waterBlastEffect[2].damageFactor=0.111000
    dbObj.waterBlastEffect[3].effectLevel=129.977005
    dbObj.waterBlastEffect[3].damageFactor=0.125000
    dbObj.waterBlastEffect[4].effectLevel=200.169006
    dbObj.waterBlastEffect[4].damageFactor=0.143000
    dbObj.waterBlastEffect[5].effectLevel=304.153992
    dbObj.waterBlastEffect[5].damageFactor=0.167000
    dbObj.waterBlastEffect[6].effectLevel=455.449005
    dbObj.waterBlastEffect[6].damageFactor=0.200000
    dbObj.waterBlastEffect[7].effectLevel=671.343018
    dbObj.waterBlastEffect[7].damageFactor=0.250000
    dbObj.waterBlastEffect[8].effectLevel=973.611023
    dbObj.waterBlastEffect[8].damageFactor=0.333000
    dbObj.waterBlastEffect[9].effectLevel=1392.737061
    dbObj.waterBlastEffect[9].damageFactor=0.500000
    dbObj.waterBlastEffect[10].effectLevel=2006.001953
    dbObj.waterBlastEffect[10].damageFactor=1.000000
    dbObj.waterBlastEffect[11].effectLevel=2519.823975
    dbObj.waterBlastEffect[11].damageFactor=2.000000
    dbObj.waterBlastEffect[12].effectLevel=3024.135986
    dbObj.waterBlastEffect[12].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*21
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=1500.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=3000.000000
    dbObj.fragEffect[2].damageFactor=0.015870
    dbObj.fragEffect[3].effectLevel=6000.000000
    dbObj.fragEffect[3].damageFactor=0.022450
    dbObj.fragEffect[4].effectLevel=10000.000000
    dbObj.fragEffect[4].damageFactor=0.028980
    dbObj.fragEffect[5].effectLevel=30000.000000
    dbObj.fragEffect[5].damageFactor=0.050190
    dbObj.fragEffect[6].effectLevel=60000.000000
    dbObj.fragEffect[6].damageFactor=0.070990
    dbObj.fragEffect[7].effectLevel=100000.000000
    dbObj.fragEffect[7].damageFactor=0.091640
    dbObj.fragEffect[8].effectLevel=300000.000000
    dbObj.fragEffect[8].damageFactor=0.158730
    dbObj.fragEffect[9].effectLevel=600000.000000
    dbObj.fragEffect[9].damageFactor=0.224480
    dbObj.fragEffect[10].effectLevel=1000000.000000
    dbObj.fragEffect[10].damageFactor=0.289800
    dbObj.fragEffect[11].effectLevel=3000000.000000
    dbObj.fragEffect[11].damageFactor=0.501950
    dbObj.fragEffect[12].effectLevel=6000000.000000
    dbObj.fragEffect[12].damageFactor=0.709860
    dbObj.fragEffect[13].effectLevel=10000000.000000
    dbObj.fragEffect[13].damageFactor=0.916420
    dbObj.fragEffect[14].effectLevel=30000000.000000
    dbObj.fragEffect[14].damageFactor=1.587290
    dbObj.fragEffect[15].effectLevel=60000000.000000
    dbObj.fragEffect[15].damageFactor=2.244770
    dbObj.fragEffect[16].effectLevel=100000000.000000
    dbObj.fragEffect[16].damageFactor=2.897980
    dbObj.fragEffect[17].effectLevel=300000000.000000
    dbObj.fragEffect[17].damageFactor=5.019450
    dbObj.fragEffect[18].effectLevel=600000000.000000
    dbObj.fragEffect[18].damageFactor=7.098570
    dbObj.fragEffect[19].effectLevel=1000000000.000000
    dbObj.fragEffect[19].damageFactor=9.164220
    dbObj.fragEffect[20].effectLevel=3000000000.000000
    dbObj.fragEffect[20].damageFactor=15.872900
    dbObj.radEffect=[pygcb.DamagePoint()]*5
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=15000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=20000.000000
    dbObj.radEffect[2].damageFactor=1.000000
    dbObj.radEffect[3].effectLevel=40000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=60000.000000
    dbObj.radEffect[4].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*7
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.420070
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.839760
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=1.680560
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=3.360580
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=6.721030
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=13.439870
    return dbObj
