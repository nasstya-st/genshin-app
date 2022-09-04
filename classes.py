# from PyQt5 import QtWidgets, uic, QtCore, QtGui
# import sys
import enum
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from app import Ui_MainWindow
# from main import Window
from dataclasses import *


class Talents(enum.Enum):
    freedom = 1
    prosperity = 2
    transience = 3
    resistance = 4
    ballad = 5
    diligence = 6
    gold = 7
    elegance = 8
    light = 9
    admonition = 10
    ingenuity = 11
    praxis = 12


class Gems(enum.Enum):
    anemo = 1
    pyro = 2
    geo = 3
    hydro = 4
    cryo = 5
    electro = 6
    dendro = 7


Locals = enum.Enum(value='Locals',
                   names=("calla_lily cecilia dandelion_seed philanemo_mushroom lamp_grass valberry yellow_lotus " 
                          "windwheel_aster wolfhook cor_lapis glaze_lily jueyun_chili noctilucous_jade qingxin "
                          "silk_flower starconch violetgrass amakumo_fruit crystall_marrow dendrobium padisarah "
                          "fluorescent_fungus naku_weed onikabuto sakura_bloom sango_pearl sea_ganoderma blue_lotus "
                          "rukkhashava")
                   )


Boss = enum.Enum(value="Boss",
                 names="geo_cube pyro_cube cryo_cube hydro_cube electro_cube anemo_cube cryo_plant pyro_plant serpent "
                       "hydro_oceanid geovishap maguu_kenki mech_array electro_oceanid wolflord coral_defenders beak "
                       "electro_plant"
                 )

Boss_tals = enum.Enum(value='Boss_tals',
                      names="dvalin_plume dvalin_claw dvalin_sigh boreas_tail boreas_ring boreas_spirit childe_tusk "
                            "childe_shard childe_shadow azhdaha_crown azhdaha_branch azhdaha_scale signora_moment "
                            "signora_butterfly signora_heart raiden_mudra raiden_tears raiden_meaning"
                      )
Enemies_gen = enum.Enum(value='Enemies_gen',
                        names=("slime hilichurl_mask samachurl hilichurl_arrow fatui treasure_hoarder whopperflower "
                               "nobushi spectral fungi_gen eremites")
                        )

Enemies_elite = enum.Enum(value='Enemies_elite',
                          names="hilichurl_horn ley_line chaos_part mist knives bone chaos_sentinel prism fungi_el "
                                "riftwolf statuette drake_chaos"
                          )

Asc_weap = enum.Enum(value='Asc_weap',
                     names="decarabian boreal gladiator guyun elixir aerosiderite branch narukami mask talisman oasis "
                           "might")


@dataclass
class Character(object):   # для проверок в функциях
    gems: Gems
    talent_book: Talents
    local: Locals
    enemie: Enemies_gen
    boss: Boss
    boss_tal: Boss_tals


@dataclass
class Char_info(object):
    clvl: int
    rlvl: int
    casc: int
    rasc: int
    ctal1: int
    ctal2: int
    ctal3: int
    rtal1: int
    rtal2: int
    rtal3: int


@dataclass
class Weapon(object):
    rarity: int
    asc: Asc_weap
    enemie_elite: Enemies_elite
    enemie_gen: Enemies_gen


@dataclass
class Weap_info(object):
    clvl: int
    rlvl: int
    casc: int
    rasc: int


# ______________________________________________________________________________________________________________________
# Characters list
chars_names4 = sorted(['Sayu', 'Sucrose', 'Chongyun', 'Diona', 'Kaeya', 'Rosaria', 'Beidou', 'Fischl', 'Sara', 'Kuki',
                      'Lisa', 'Razor', 'Gorou', 'Ningguang', 'Noelle', 'Yun_Jin', 'Barbara', 'Xingqiu', 'Amber',
                      'Bennett', 'Thoma', 'Xiangling', 'Xinyan', 'Yanfei', 'Heizou', 'Collei', 'Dori'])
chars_names5 = sorted(['Jean', 'Kazuha', 'Venti', 'Xiao', 'Aloy', 'Eula', 'Ganyu', 'Ayaka', 'Qiqi', 'Shenhe', 'Keqing',
                       'Raiden', 'Yae_Miko', 'Albedo', 'Itto', 'Zhongli', 'Ayato', 'Mona', 'Kokomi', 'Tartaglia',
                       'Yelan', 'Diluc', 'Hu_Tao', 'Klee', 'Yoimiya', 'Tighnari'])
# ______________________________________________________________________________________________________________________
# Weapons lists
bows = sorted(["Skyward_Harp", "Amos'_Bow", "Alley_Hunter", "The_Viridescent_Hunt", "The_Stringless", "Sacrificial_Bow",
               "Rust", "Royal_Bow", "Prototype_Crescent", "Mouun's_Moon", "Mitternachts_Waltz", "Hamayumi",
               "Favonius_Warbow", "Fading_Twilight", "Compound_Bow", "Blackcliff_Warbow"])
catalysts = sorted(["Blackcliff_Agate", "The_Widsith", "Solar_Pearl", "Royal_Grimoire", "Sacrificial_Fragments",
                    "Prototype_Amber", "Oathsworn_Eye", "Wine_and_Song", "Mappa_Mare", "Hakushin_Ring", "Frostbearer",
                    "Favonius_Codex", "Eye_of_Perception", "Dodoco_Tales", 'Lost_Prayer_to_the_Sacred_Winds'])
polearms = sorted(["Staff_of_Homa", "Prototype_Starglitter", "Lithic_Spear", "The_Cath", "Crescent_Pike",
                   "Favonius_Lance", "Dragonspine_Spear", "Deathmatch", "Dragon's_Bane", "Kitain_Cross_Spear",
                   "Blackcliff_Pole", "Royal_Spear", "Wavebreaker's_Fin", "Primordial_Jade_Winged-Spear"])
claymores = sorted(["Redhorn_Stonethresher", "Whiteblind", "The_Bell", "Serpent_Spine", "Snow-Tombed_Starsilver",
                    "Sacrificial_Greatsword", "Lithic_Blade", "Blackcliff_Slasher", "Rainslasher", "Prototype_Archaic",
                    "Akuoumaru", "Luxurious_Sea-Lord", "Katsuragikiri_Nagamasa", "Favonius_Greatsword",
                    "Royal_Greatsword", "Forest_Regalia"])
swords = sorted(["Amenoma_Kageuchi", "The_Black_Sword", "The_Alley_Flash",  "Royal_Longsword", 'Kagotsurube_Isshin',
                 "Sacrificial_Sword", "The_Flute", "Iron_String", "Prototype_Rancour", "Lion's_Roar", "Freedom-Sworn",
                 "Favonius_Sword", "Cinnabar_Spindle", "Blackcliff_Longsword", 'The_Black_Sword', "Sapwood_Blade"])
# ______________________________________________________________________________________________________________________
# all characters and their resources
all_chars = {'Amber': Character(Gems.pyro, Talents.freedom, Locals.lamp_grass, Enemies_gen.hilichurl_arrow,
                                Boss.pyro_plant, Boss_tals.dvalin_sigh),
             'Albedo': Character(Gems.geo, Talents.ballad, Locals.cecilia, Enemies_gen.samachurl, Boss.geo_cube,
                                 Boss_tals.childe_tusk),
             'Aloy': Character(Gems.cryo, Talents.freedom, Locals.crystall_marrow, Enemies_gen.spectral, Boss.cryo_cube,
                               Boss_tals.signora_moment),
             'Itto': Character(Gems.geo, Talents.elegance, Locals.onikabuto, Enemies_gen.slime, Boss.wolflord,
                               Boss_tals.signora_heart),
             'Barbara': Character(Gems.hydro, Talents.freedom, Locals.philanemo_mushroom, Enemies_gen.samachurl,
                                  Boss.hydro_oceanid, Boss_tals.boreas_ring),
             'Beidou': Character(Gems.electro, Talents.gold, Locals.noctilucous_jade, Enemies_gen.treasure_hoarder,
                                 Boss.electro_cube, Boss_tals.dvalin_sigh),
             'Bennett': Character(Gems.pyro, Talents.resistance, Locals.windwheel_aster, Enemies_gen.treasure_hoarder,
                                  Boss.pyro_plant, Boss_tals.dvalin_plume),
             'Chongyun': Character(Gems.cryo, Talents.diligence, Locals.cor_lapis, Enemies_gen.hilichurl_mask,
                                   Boss.cryo_plant, Boss_tals.dvalin_sigh),
             'Diluc': Character(Gems.pyro, Talents.resistance, Locals.lamp_grass, Enemies_gen.fatui, Boss.pyro_plant,
                                Boss_tals.dvalin_plume),
             'Diona': Character(Gems.cryo, Talents.freedom, Locals.calla_lily, Enemies_gen.hilichurl_arrow,
                                Boss.cryo_plant, Boss_tals.childe_shard),
             'Fischl': Character(Gems.electro, Talents.ballad, Locals.lamp_grass, Enemies_gen.hilichurl_arrow,
                                 Boss.electro_cube, Boss_tals.boreas_spirit),
             'Ganyu': Character(Gems.cryo, Talents.diligence, Locals.qingxin, Enemies_gen.whopperflower,
                                Boss.cryo_plant, Boss_tals.childe_shadow),
             'Gorou': Character(Gems.geo, Talents.light, Locals.sango_pearl, Enemies_gen.spectral, Boss.mech_array,
                                Boss_tals.signora_moment),
             'Hu_Tao': Character(Gems.pyro, Talents.diligence, Locals.silk_flower, Enemies_gen.whopperflower,
                                 Boss.geovishap, Boss_tals.childe_shard),
             'Jean': Character(Gems.anemo, Talents.resistance, Locals.dandelion_seed, Enemies_gen.hilichurl_mask,
                               Boss.anemo_cube, Boss_tals.dvalin_plume),
             'Kazuha': Character(Gems.anemo, Talents.diligence, Locals.sea_ganoderma, Enemies_gen.treasure_hoarder,
                                 Boss.maguu_kenki, Boss_tals.azhdaha_scale),
             'Kaeya': Character(Gems.cryo, Talents.ballad, Locals.calla_lily, Enemies_gen.treasure_hoarder,
                                Boss.cryo_plant, Boss_tals.boreas_spirit),
             'Ayaka': Character(Gems.cryo, Talents.elegance, Locals.sakura_bloom, Enemies_gen.nobushi, Boss.mech_array,
                                Boss_tals.azhdaha_branch),
             'Ayato': Character(Gems.cryo, Talents.elegance, Locals.sakura_bloom, Enemies_gen.nobushi, Boss.hydro_cube,
                                Boss_tals.raiden_mudra),
             'Keqing': Character(Gems.electro, Talents.prosperity, Locals.cor_lapis, Enemies_gen.whopperflower,
                                 Boss.electro_cube, Boss_tals.boreas_ring),
             'Klee': Character(Gems.pyro, Talents.freedom, Locals.philanemo_mushroom, Enemies_gen.samachurl,
                               Boss.pyro_plant, Boss_tals.boreas_ring),
             "Sara": Character(Gems.electro, Talents.elegance, Locals.dendrobium, Enemies_gen.hilichurl_mask,
                               Boss.electro_oceanid, Boss_tals.signora_heart),
             "Kuki": Character(Gems.electro, Talents.elegance, Locals.naku_weed, Enemies_gen.spectral, Boss.serpent,
                               Boss_tals.raiden_tears),
             "Lisa": Character(Gems.electro, Talents.ballad, Locals.valberry, Enemies_gen.slime, Boss.electro_cube,
                               Boss_tals.dvalin_claw),
             "Mona": Character(Gems.hydro, Talents.resistance, Locals.philanemo_mushroom, Enemies_gen.whopperflower,
                               Boss.hydro_oceanid, Boss_tals.boreas_ring),
             'Ningguang': Character(Gems.geo, Talents.prosperity, Locals.glaze_lily, Enemies_gen.fatui, Boss.geo_cube,
                                    Boss_tals.boreas_spirit),
             'Noelle': Character(Gems.geo, Talents.resistance, Locals.valberry, Enemies_gen.hilichurl_mask,
                                 Boss.geo_cube, Boss_tals.dvalin_claw),
             'Qiqi': Character(Gems.cryo, Talents.prosperity, Locals.violetgrass, Enemies_gen.samachurl,
                               Boss.cryo_plant, Boss_tals.boreas_tail),
             'Raiden': Character(Gems.electro, Talents.light, Locals.amakumo_fruit, Enemies_gen.nobushi,
                                 Boss.electro_oceanid, Boss_tals.signora_moment),
             'Razor': Character(Gems.electro, Talents.resistance, Locals.wolfhook, Enemies_gen.hilichurl_mask,
                                Boss.electro_cube, Boss_tals.dvalin_claw),
             'Rosaria': Character(Gems.cryo, Talents.ballad, Locals.valberry, Enemies_gen.fatui, Boss.cryo_plant,
                                  Boss_tals.childe_shadow),
             'Kokomi': Character(Gems.hydro, Talents.transience, Locals.sango_pearl, Enemies_gen.spectral,
                                 Boss.hydro_cube, Boss_tals.signora_butterfly),
             'Sayu': Character(Gems.anemo, Talents.light, Locals.crystall_marrow, Enemies_gen.whopperflower,
                               Boss.maguu_kenki, Boss_tals.azhdaha_scale),
             'Shenhe': Character(Gems.cryo, Talents.prosperity, Locals.qingxin, Enemies_gen.whopperflower,
                                 Boss.coral_defenders, Boss_tals.signora_butterfly),
             'Heizou': Character(Gems.anemo, Talents.transience, Locals.onikabuto, Enemies_gen.treasure_hoarder,
                                 Boss.serpent, Boss_tals.raiden_meaning),
             'Sucrose': Character(Gems.anemo, Talents.freedom, Locals.windwheel_aster, Enemies_gen.whopperflower,
                                  Boss.anemo_cube, Boss_tals.boreas_spirit),
             'Tartaglia': Character(Gems.hydro, Talents.freedom, Locals.starconch, Enemies_gen.fatui,
                                    Boss.hydro_oceanid, Boss_tals.childe_shard),
             'Thoma': Character(Gems.pyro, Talents.transience,  Locals.fluorescent_fungus, Enemies_gen.treasure_hoarder,
                                Boss.pyro_cube, Boss_tals.signora_butterfly),
             'Xiangling': Character(Gems.pyro, Talents.diligence, Locals.jueyun_chili, Enemies_gen.slime,
                                    Boss.pyro_plant, Boss_tals.dvalin_claw),
             'Xiao': Character(Gems.anemo, Talents.prosperity, Locals.qingxin, Enemies_gen.slime, Boss.geovishap,
                               Boss_tals.childe_shadow),
             'Xingqiu': Character(Gems.hydro, Talents.gold, Locals.silk_flower, Enemies_gen.hilichurl_mask,
                                  Boss.hydro_oceanid, Boss_tals.boreas_tail),
             'Xinyan': Character(Gems.pyro, Talents.gold, Locals.violetgrass, Enemies_gen.treasure_hoarder,
                                 Boss.pyro_plant, Boss_tals.childe_tusk),
             'Yae_Miko': Character(Gems.electro, Talents.light, Locals.sea_ganoderma, Enemies_gen.nobushi,
                                   Boss.coral_defenders, Boss_tals.raiden_meaning),
             'Yanfei': Character(Gems.pyro, Talents.gold, Locals.noctilucous_jade, Enemies_gen.treasure_hoarder,
                                 Boss.geovishap, Boss_tals.azhdaha_branch),
             'Yelan': Character(Gems.hydro, Talents.prosperity, Locals.starconch, Enemies_gen.fatui, Boss.serpent,
                                Boss_tals.azhdaha_scale),
             'Yoimiya': Character(Gems.pyro, Talents.transience, Locals.naku_weed, Enemies_gen.samachurl,
                                 Boss.pyro_cube, Boss_tals.azhdaha_crown),
             'Yun_Jin': Character(Gems.geo, Talents.diligence, Locals.glaze_lily, Enemies_gen.hilichurl_mask,
                                  Boss.wolflord, Boss_tals.signora_heart),
             'Zhongli': Character(Gems.geo, Talents.gold, Locals.cor_lapis, Enemies_gen.slime, Boss.geo_cube,
                                  Boss_tals.childe_tusk),
             'Collei': Character(Gems.dendro, Talents.praxis, Locals.rukkhashava, Enemies_gen.hilichurl_arrow,
                                 Boss.beak, Boss_tals.raiden_tears),
             'Dori': Character(Gems.electro, Talents.ingenuity, Locals.blue_lotus, Enemies_gen.eremites,
                               Boss.electro_plant, Boss_tals.azhdaha_branch),
             'Tighnari': Character(Gems.dendro, Talents.admonition, Locals.yellow_lotus, Enemies_gen.fungi_gen,
                                   Boss.beak, Boss_tals.raiden_meaning)
             }
# ______________________________________________________________________________________________________________________
# Dict with all weapon and its resources
all_weap = {"Skyward_Blade": Weapon(5, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.slime),
            'Freedom_Sworn': Weapon(5, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.samachurl),
            "The_Flute": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.slime),
            "The_Black_Sword": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.slime),
            "The_Alley_Flash": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.samachurl),
            "Sacrificial_Sword": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.samachurl),
            "Royal_Longsword": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.hilichurl_arrow),
            "Prototype_Rancour": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.fatui),
            "Amenoma_Kageuchi": Weapon(4, Asc_weap.branch, Enemies_elite.chaos_sentinel, Enemies_gen.nobushi),
            "Lions_Roar": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.treasure_hoarder),
            "Kagotsurube_Isshin": Weapon(4, Asc_weap.mask, Enemies_elite.statuette, Enemies_gen.spectral),
            "Iron_Sting": Weapon(4, Asc_weap.aerosiderite, Enemies_elite.bone, Enemies_gen.whopperflower),
            "Favonius_Sword": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.hilichurl_arrow),
            "Cinnabar_Spindle": Weapon(4, Asc_weap.decarabian, Enemies_elite.chaos_part, Enemies_gen.hilichurl_mask),
            "Blackcliff_Longsword": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.hilichurl_arrow),
            "Skyward_Harp": Weapon(5, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.hilichurl_arrow),
            "Amos_Bow": Weapon(5, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.slime),
            "Alley_Hunter": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.slime),
            "The_Viridescent_Hunt": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn,
                                           Enemies_gen.hilichurl_arrow),
            "The_Stringless": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.hilichurl_arrow),
            "Sacrificial_Bow": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.slime),
            "Rust": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.hilichurl_mask),
            "Royal_Bow": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.samachurl),
            "Prototype_Crescent": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.treasure_hoarder),
            "Mouuns_Moon": Weapon(4, Asc_weap.narukami, Enemies_elite.prism, Enemies_gen.spectral),
            "Mitternachts_Waltz": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn,
                                         Enemies_gen.treasure_hoarder),
            "Hamayumi": Weapon(4, Asc_weap.narukami, Enemies_elite.prism, Enemies_gen.hilichurl_arrow),
            "Favonius_Warbow": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.whopperflower),
            "Fading_Twilight": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.samachurl),
            "Compound_Bow": Weapon(4, Asc_weap.guyun, Enemies_elite.bone, Enemies_gen.fatui),
            "Blackcliff_Warbow": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.whopperflower),
            "Windblume_Ode": Weapon(4, Asc_weap.gladiator, Enemies_elite.ley_line, Enemies_gen.whopperflower),
            "Redhorn_Stonethresher": Weapon(5, Asc_weap.narukami, Enemies_elite.riftwolf, Enemies_gen.nobushi),
            "Whiteblind": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.treasure_hoarder),
            "The_Bell": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.whopperflower),
            "Snow_Tombed_Starsilver": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.slime),
            "Serpent_Spine": Weapon(4, Asc_weap.aerosiderite, Enemies_elite.bone, Enemies_gen.whopperflower),
            "Sacrificial_Greatsword": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.hilichurl_arrow),
            "Blackcliff_Slasher": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.fatui),
            "Akuoumaru": Weapon(4, Asc_weap.branch, Enemies_elite.riftwolf, Enemies_gen.nobushi),
            "Rainslasher": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.samachurl),
            "Prototype_Archaic": Weapon(4, Asc_weap.aerosiderite, Enemies_elite.bone, Enemies_gen.hilichurl_mask),
            "Luxurious_Sea_Lord": Weapon(4, Asc_weap.aerosiderite, Enemies_elite.bone, Enemies_gen.slime),
            "Lithic_Blade": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.hilichurl_arrow),
            "Katsuragikiri_Nagamasa": Weapon(4, Asc_weap.narukami, Enemies_elite.chaos_sentinel, Enemies_gen.nobushi),
            "Favonius_Greatsword": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.fatui),
            "Royal_Greatsword": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.slime),
            "Lost_Prayer_to_the_Sacred_Winds": Weapon(5, Asc_weap.gladiator, Enemies_elite.chaos_part,
                                                      Enemies_gen.slime),
            "Blackcliff_Agate": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.samachurl),
            "The_Widsith": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.hilichurl_mask),
            "Solar_Pearl": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.whopperflower),
            "Sacrificial_Fragments": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part,
                                            Enemies_gen.treasure_hoarder),
            "Royal_Grimoire": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.fatui),
            "Oathsworn_Eye": Weapon(4, Asc_weap.branch, Enemies_elite.riftwolf, Enemies_gen.spectral),
            "Wine_and_Song": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.treasure_hoarder),
            "Mappa_Mare": Weapon(4, Asc_weap.aerosiderite, Enemies_elite.bone, Enemies_gen.slime),
            "Hakushin_Ring": Weapon(4, Asc_weap.branch, Enemies_elite.prism, Enemies_gen.samachurl),
            "Frostbearer": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.whopperflower),
            "Favonius_Codex": Weapon(4, Asc_weap.decarabian, Enemies_elite.hilichurl_horn, Enemies_gen.samachurl),
            "Eye_of_Perception": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.hilichurl_mask),
            "Dodoco_Tales": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.hilichurl_mask),
            "Prototype_Amber": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.hilichurl_arrow),
            "Primordial_Jade_Winged_Spear": Weapon(5, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.fatui),
            "Staff_of_Homa": Weapon(5, Asc_weap.aerosiderite, Enemies_elite.ley_line, Enemies_gen.slime),
            "Prototype_Starglitter": Weapon(4, Asc_weap.aerosiderite, Enemies_elite.bone, Enemies_gen.hilichurl_mask),
            "Lithic_Spear": Weapon(4, Asc_weap.aerosiderite, Enemies_elite.bone, Enemies_gen.hilichurl_arrow),
            "Kitain_Cross_Spear": Weapon(4, Asc_weap.mask, Enemies_elite.chaos_sentinel, Enemies_gen.treasure_hoarder),
            "The_Catch": Weapon(4, Asc_weap.mask, Enemies_elite.chaos_sentinel, Enemies_gen.spectral),
            "Deathmatch": Weapon(4, Asc_weap.boreal, Enemies_elite.ley_line, Enemies_gen.whopperflower),
            "Crescent_Pike": Weapon(4, Asc_weap.guyun, Enemies_elite.knives, Enemies_gen.treasure_hoarder),
            "Blackcliff_Pole": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.fatui),
            "Wavebreakers_Fin": Weapon(4, Asc_weap.mask, Enemies_elite.riftwolf, Enemies_gen.nobushi),
            "Royal_Spear": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.fatui),
            "Favonius_Lance": Weapon(4, Asc_weap.gladiator, Enemies_elite.chaos_part, Enemies_gen.slime),
            "Dragonspine_Spear": Weapon(4, Asc_weap.boreal, Enemies_elite.mist, Enemies_gen.fatui),
            "Dragons_Bane": Weapon(4, Asc_weap.elixir, Enemies_elite.mist, Enemies_gen.samachurl),
            "Forest_Regalia": Weapon(4, Asc_weap.talisman, Enemies_elite.drake_chaos, Enemies_gen.eremites),
            "Sapwood_Blade": Weapon(4, Asc_weap.talisman, Enemies_elite.drake_chaos, Enemies_gen.eremites)
            }
# ______________________________________________________________________________________________________________________
# Dict with all chosen characters
chosen = {}
# Dict with all added buttons
added = {}
# Dict with all chosen weapon
chosen_w = {}
# Dict with all added weapon buttons
added_w = {}
# Dict with used at this moment resources
resources = {'total_exp': 0, 'exp_weapon': 0, 'total_mora': 0, 'crystal_exp': [0, 0, 0, 0], 'book_exp': [0, 0, 0, 0]}
# Information about user's inventory content
having = {}
# Spinboxes, labels, sometimes buttons (resources)
cont = {}
# Dicts with QActions
actions_chars = {}
actions_weap = {}

# Lists with the amounts of required materials for chars
mora_asc = [x for x in range(20000, 120001, 20000)]
mora_tals = (0, 12500, 17500, 25000, 30000, 37500, 120000, 260000, 450000, 700000)
local = (3, 10, 20, 30, 45, 60)
boss = (0, 2, 4, 8, 12, 20)
gems = (1, 3, 6, 3, 6, 6)
enemies_asc = (3, 15, 12, 18, 12, 24)
enemies_tals = (0, 6, 3, 4, 6, 9, 4, 6, 9, 12)
books_tals = (0, 3, 2, 4, 6, 9, 4, 6, 12, 16)
boss_tals = (0, 0, 0, 0, 0, 0, 1, 1, 2, 2)
exp_lvl = (0, 1000, 1325, 1700, 2150, 2625, 3150, 3725, 4350, 5000, 5700, 6450, 7225, 8050, 8925, 9825, 10750, 11725,
           12725, 13775, 14875, 16800, 18000, 19250, 20550, 21875, 23250, 24650, 26100, 27575, 29100, 30650, 32250,
           33875, 35550, 37250, 38975, 40750, 42575, 44425, 46300, 50625, 52700, 54775, 56900, 59075, 61275, 63525,
           65800, 68125, 70475, 76500, 79050, 81650, 84275, 86950, 89650, 92400, 95175, 98000, 100875, 108950, 112050,
           115175, 118325, 121525, 124775, 128075, 131400, 134775, 138175, 148700, 152375, 156075, 159825, 163600,
           167425, 171300, 175225, 179175, 183175, 216225, 243025, 273100, 306800, 344600, 386950, 434425, 487625,
           547200)
# And for weapon
exp_weap = (0, 400, 625, 900, 1200, 1550, 1950, 2350, 2800, 3300, 3800, 4350, 4925, 5525, 6150, 6800, 7500, 8200, 8950,
            9725, 10500, 11900, 12775, 13700, 14650, 15625, 16625, 17650, 18700, 19775, 20900, 22025, 23200, 24375,
            25600, 26825, 28100, 29400, 30725, 32075, 33425, 36575, 38075, 39600, 41150, 42725, 44325, 45950, 47600,
            49300, 51000, 55375, 57225, 59100, 61025, 62950, 64925, 66900, 68925, 70975, 73050, 78900, 81125, 83400,
            85700, 88025, 90375, 92750, 95150, 97575, 100050, 107675, 110325, 113000, 115700, 118425, 121200, 124000,
            126825, 129675, 132575, 156475, 175875, 197600, 221975, 249300, 279950, 314250, 352700, 395775)

dange4 = (3, 3, 6, 3, 6, 4)
enemies_elite4 = (3, 12, 6, 12, 9, 18)
enemies_gen4 = (2, 8, 6, 9, 6, 12)
mora_asc_w4 = (5000, 15000, 20000, 30000, 35000, 45000)
enemies_gen5 = (5, 18, 9, 18, 14, 27)
enemies_elite5 = (3, 12, 9, 14, 9, 18)
mora_asc_w5 = (10000, 20000, 30000, 45000, 55000, 65000)
dange5 = (5, 5, 9, 5, 9, 6)

# ______________________________________________________________________________________________________________________
