from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

mod=Mod('Garcia_Full_Auto.bl3hotfix',
'Garcia goes RATATATATATA',
'Grimm',
[
    'Categories: gear-shotgun',
    'Makes the Garcia shotgun fully automatic.',
    'The gun has to be re looted since it now spawns with different parts to allow it to be full auto.',
    'The recoil has been ajusted so it doesn"t fo flying on two hits.',
    'It now only consummes one ammo per shot, but the damage has been untouched (it may new be "a bit" op).'
],
lic=Mod.CC_BY_SA_40,
)

mod.comment('Recoil Scale')
if True:

    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Barrel_Garcia.Part_SG_JAK_Barrel_Garcia',
    'InventoryAttributeEffects.InventoryAttributeEffects[5]',
    """
    (
        AttributeToModify=GbxAttributeData'"/Game/GameData/Weapons/Att_Weapon_RecoilHeightScale.Att_Weapon_RecoilHeightScale"',
        ModifierType=ScaleSimple,
        ModifierValue=(BaseValueConstant=0.2,DataTableValue=(DataTable=None,RowName=None,ValueName=None),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.0)
    )
    """
    )
    mod.newline()

mod.comment('Fire Rate')
if True:

    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Barrel_Garcia.Part_SG_JAK_Barrel_Garcia',
    'AspectList.AspectList[0].Object..WeaponUseComponent.Object..FireRate.BaseValue',
    8.0
    )
    mod.newline()

mod.comment('Making it Full Auto')
if True:

    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Barrel_Garcia.Part_SG_JAK_Barrel_Garcia',
    'AspectList.AspectList[0].Object..WeaponUseComponent.Object..AutomaticBurstCount.BaseValue',
    0.0
    )
    mod.newline()

mod.comment('Modifying the Garcia Material')
if True:

    mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Material_Garcia',
    'ApsectList.AspectList[1].Object..Material',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/Model/Materials/Unique/MI_PS_Jak_Bekah.MI_PS_Jak_Bekah'
    )
    mod.newline()

mod.comment('Unlocking the Garcia')
if True:

    mod.comment('PartSet')
    if True:

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/PartSet_SG_JAK_Garcia',
        'ActorPartLists',
        """
        (
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=0,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=2,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=3,bCanSelectMultipleParts=True,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=2),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=4,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=False,Parts=()),    
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=5,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=6,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=7,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()), 
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=8,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=9,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=10,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=()),
            (PartTypeEnum=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/EPartList_Jakobs_Shotgun.EPartList_Jakobs_Shotgun,PartType=11,bCanSelectMultipleParts=False,bUseWeightWithMultiplePartSelection=False,MultiplePartSelectionRange=(Min=0,Max=0),bEnabled=True,Parts=())
        )
        """
        )
        mod.newline()

    mod.comment('Balance TOC')
    if True:

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia',
        'RuntimePartList.PartTypeTOC',
        """
        (
            (
                StartIndex=0,
                NumParts=1
            ),
            (
                StartIndex=1,
                NumParts=3
            ),
            (
                StartIndex=4,
                NumParts=1
            ),
            (
                StartIndex=5,
                NumParts=2
            ),
            (
                StartIndex=7,
                NumParts=0
            ),
            (
                StartIndex=7,
                NumParts=5
            ),
            (
                StartIndex=12,
                NumParts=5
            ),
            (
                StartIndex=17,
                NumParts=5
            ),
            (
                StartIndex=22,
                NumParts=5
            ),
            (
                StartIndex=27,
                NumParts=3
            ),
            (
                StartIndex=30,
                NumParts=4
            ),
            (
                StartIndex=34,
                NumParts=1
            )
        )
        """
        )
        mod.newline()

    mod.comment('Balance')
    if True:

        mod.reg_hotfix(Mod.EARLYLEVEL,'MatchAll',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia',
        'RuntimePartList.AllParts',
        """
        (
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Body/Part_SG_JAK_Body.Part_SG_JAK_Body,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Body/Part_SG_JAK_Trigger_01.Part_SG_JAK_Trigger_01,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Body/Part_SG_JAK_Trigger_02.Part_SG_JAK_Trigger_02,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Body/Part_SG_JAK_Trigger_03.Part_SG_JAK_Trigger_03,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Barrel_Garcia.Part_SG_JAK_Barrel_Garcia,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_JAK_Barrel_01_A.Part_SG_JAK_Barrel_01_A,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Barrel/Barrel_01/Part_SG_JAK_Barrel_01_C.Part_SG_JAK_Barrel_01_C,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Bolt/Part_SG_JAK_Bolt_01.Part_SG_JAK_Bolt_01,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Bolt/Part_SG_JAK_Bolt_02.Part_SG_JAK_Bolt_02,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Bolt/Part_SG_JAK_Bolt_03.Part_SG_JAK_Bolt_03,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Bolt/Part_SG_JAK_Bolt_04.Part_SG_JAK_Bolt_04,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Bolt/Part_SG_JAK_Bolt_05.Part_SG_JAK_Bolt_05,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Foregrip/Part_SG_JAK_Foregrip_01.Part_SG_JAK_Foregrip_01,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Foregrip/Part_SG_JAK_Foregrip_02.Part_SG_JAK_Foregrip_02,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Foregrip/Part_SG_JAK_Foregrip_03.Part_SG_JAK_Foregrip_03,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Foregrip/Part_SG_JAK_Foregrip_04.Part_SG_JAK_Foregrip_04,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Foregrip/Part_SG_JAK_Foregrip_05.Part_SG_JAK_Foregrip_05,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_01.Part_SG_JAK_Stock_01,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_02.Part_SG_JAK_Stock_02,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_03.Part_SG_JAK_Stock_03,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_04.Part_SG_JAK_Stock_04,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_05.Part_SG_JAK_Stock_05,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_01_A.Part_SG_JAK_Stock_01_A,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_02_A.Part_SG_JAK_Stock_02_A,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_03_A.Part_SG_JAK_Stock_03_A,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_04_A.Part_SG_JAK_Stock_04_A,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Stock/Part_SG_JAK_Stock_05_A.Part_SG_JAK_Stock_05_A,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Magazine/Part_SG_JAK_Mag_01.Part_SG_JAK_Mag_01,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Magazine/Part_SG_JAK_Mag_02.Part_SG_JAK_Mag_02,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Magazine/Part_SG_JAK_Mag_03.Part_SG_JAK_Mag_03,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Scope/Part_SG_JAK_IronSight.Part_SG_JAK_IronSight,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Scope/Part_SG_JAK_Scope_01.Part_SG_JAK_Scope_01,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Scope/Part_SG_JAK_Scope_02.Part_SG_JAK_Scope_02,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/Parts/Scope/Part_SG_JAK_Scope_03.Part_SG_JAK_Scope_03,Weight=(BaseValueConstant=1.0)),
            (PartData=/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Parts/Part_SG_JAK_Material_Garcia.Part_SG_JAK_Material_Garcia,Weight=(BaseValueConstant=1.0))
        )
        """
        )
        mod.newline()
