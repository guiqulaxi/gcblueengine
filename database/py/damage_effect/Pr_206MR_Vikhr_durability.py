# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Pr 206MR Vikhr durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.740000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.830000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.090000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=3.510000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=4.110000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=4.880000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=5.830000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=6.940000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=8.220000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=9.680000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=11.310000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=14.250000
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*25
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=67.974998
    dbObj.waterBlastEffect[1].damageFactor=0.045000
    dbObj.waterBlastEffect[2].effectLevel=77.182999
    dbObj.waterBlastEffect[2].damageFactor=0.048000
    dbObj.waterBlastEffect[3].effectLevel=87.595001
    dbObj.waterBlastEffect[3].damageFactor=0.050000
    dbObj.waterBlastEffect[4].effectLevel=99.364998
    dbObj.waterBlastEffect[4].damageFactor=0.053000
    dbObj.waterBlastEffect[5].effectLevel=112.665001
    dbObj.waterBlastEffect[5].damageFactor=0.056000
    dbObj.waterBlastEffect[6].effectLevel=127.692001
    dbObj.waterBlastEffect[6].damageFactor=0.059000
    dbObj.waterBlastEffect[7].effectLevel=144.669998
    dbObj.waterBlastEffect[7].damageFactor=0.062000
    dbObj.waterBlastEffect[8].effectLevel=163.852005
    dbObj.waterBlastEffect[8].damageFactor=0.067000
    dbObj.waterBlastEffect[9].effectLevel=185.533005
    dbObj.waterBlastEffect[9].damageFactor=0.071000
    dbObj.waterBlastEffect[10].effectLevel=210.054993
    dbObj.waterBlastEffect[10].damageFactor=0.077000
    dbObj.waterBlastEffect[11].effectLevel=237.819000
    dbObj.waterBlastEffect[11].damageFactor=0.083000
    dbObj.waterBlastEffect[12].effectLevel=269.304993
    dbObj.waterBlastEffect[12].damageFactor=0.091000
    dbObj.waterBlastEffect[13].effectLevel=305.098999
    dbObj.waterBlastEffect[13].damageFactor=0.100000
    dbObj.waterBlastEffect[14].effectLevel=345.937012
    dbObj.waterBlastEffect[14].damageFactor=0.111000
    dbObj.waterBlastEffect[15].effectLevel=392.777008
    dbObj.waterBlastEffect[15].damageFactor=0.125000
    dbObj.waterBlastEffect[16].effectLevel=446.921997
    dbObj.waterBlastEffect[16].damageFactor=0.143000
    dbObj.waterBlastEffect[17].effectLevel=510.259003
    dbObj.waterBlastEffect[17].damageFactor=0.167000
    dbObj.waterBlastEffect[18].effectLevel=585.729004
    dbObj.waterBlastEffect[18].damageFactor=0.200000
    dbObj.waterBlastEffect[19].effectLevel=678.408020
    dbObj.waterBlastEffect[19].damageFactor=0.250000
    dbObj.waterBlastEffect[20].effectLevel=798.377014
    dbObj.waterBlastEffect[20].damageFactor=0.333000
    dbObj.waterBlastEffect[21].effectLevel=970.492981
    dbObj.waterBlastEffect[21].damageFactor=0.500000
    dbObj.waterBlastEffect[22].effectLevel=1287.530029
    dbObj.waterBlastEffect[22].damageFactor=1.000000
    dbObj.waterBlastEffect[23].effectLevel=1660.525024
    dbObj.waterBlastEffect[23].damageFactor=2.000000
    dbObj.waterBlastEffect[24].effectLevel=2121.492920
    dbObj.waterBlastEffect[24].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*20
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=76881.992188
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=100000.000000
    dbObj.fragEffect[2].damageFactor=0.016270
    dbObj.fragEffect[3].effectLevel=300000.000000
    dbObj.fragEffect[3].damageFactor=0.028170
    dbObj.fragEffect[4].effectLevel=600000.000000
    dbObj.fragEffect[4].damageFactor=0.039840
    dbObj.fragEffect[5].effectLevel=1000000.000000
    dbObj.fragEffect[5].damageFactor=0.051440
    dbObj.fragEffect[6].effectLevel=3000000.000000
    dbObj.fragEffect[6].damageFactor=0.089090
    dbObj.fragEffect[7].effectLevel=6000000.000000
    dbObj.fragEffect[7].damageFactor=0.125990
    dbObj.fragEffect[8].effectLevel=10000000.000000
    dbObj.fragEffect[8].damageFactor=0.162660
    dbObj.fragEffect[9].effectLevel=30000000.000000
    dbObj.fragEffect[9].damageFactor=0.281730
    dbObj.fragEffect[10].effectLevel=60000000.000000
    dbObj.fragEffect[10].damageFactor=0.398430
    dbObj.fragEffect[11].effectLevel=100000000.000000
    dbObj.fragEffect[11].damageFactor=0.514370
    dbObj.fragEffect[12].effectLevel=300000000.000000
    dbObj.fragEffect[12].damageFactor=0.890910
    dbObj.fragEffect[13].effectLevel=600000000.000000
    dbObj.fragEffect[13].damageFactor=1.259940
    dbObj.fragEffect[14].effectLevel=1000000000.000000
    dbObj.fragEffect[14].damageFactor=1.626570
    dbObj.fragEffect[15].effectLevel=3000000000.000000
    dbObj.fragEffect[15].damageFactor=2.817310
    dbObj.fragEffect[16].effectLevel=6000000000.000000
    dbObj.fragEffect[16].damageFactor=3.984280
    dbObj.fragEffect[17].effectLevel=10000000000.000000
    dbObj.fragEffect[17].damageFactor=5.143680
    dbObj.fragEffect[18].effectLevel=30000001024.000000
    dbObj.fragEffect[18].damageFactor=8.909120
    dbObj.fragEffect[19].effectLevel=60000002048.000000
    dbObj.fragEffect[19].damageFactor=12.599390
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
    dbObj.internalEffect=[pygcb.DamagePoint()]*10
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.069190
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.138440
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.276870
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.553510
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=1.107120
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=2.214330
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=4.429110
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=8.858560
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=17.717220
    return dbObj
