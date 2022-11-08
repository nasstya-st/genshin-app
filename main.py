from PyQt5 import QtCore, QtGui, Qt, QtWidgets
import sys
import atexit
import copy
from PyQt5.QtGui import *
from PyQt5.Qt import *

from app import Ui_MainWindow
from classes import *

currNameChar = ""
currNameWeap = ''
resources = copy.deepcopy(resources_clear)


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        id = QFontDatabase.addApplicationFont(':/fonts/Genshin_Impact.ttf')
        self.fontgensh = QFontDatabase.applicationFontFamilies(id)[0]
        self.ui.menubar.setFont(QFont(self.fontgensh, 9))

        self.create_actions('characters', chars_names5, self.ui.menu5_star)
        self.create_actions('characters', chars_names4, self.ui.menu4_star)
        self.create_actions('weapon', bows, self.ui.menuBows)
        self.create_actions('weapon', catalysts, self.ui.menuCatalysts)
        self.create_actions('weapon', swords, self.ui.menuSwords)
        self.create_actions('weapon', claymores, self.ui.menuClaymores)
        self.create_actions('weapon', polearms, self.ui.menuPolearms)

        self.add_permanent_rows()

        self.setWindowTitle('Genshin resources calculator')
        self.setWindowIcon(QtGui.QIcon(f":/icons/all/icon.jpg"))
        # Setting ids for radio buttons
        self.ui.buttonGroup.setId(self.ui.rb0, 0)
        self.ui.buttonGroup.setId(self.ui.rb1, 1)
        self.ui.buttonGroup.setId(self.ui.rb2, 2)
        self.ui.buttonGroup.setId(self.ui.rb3, 3)
        self.ui.buttonGroup.setId(self.ui.rb4, 4)
        self.ui.buttonGroup.setId(self.ui.rb5, 5)
        self.ui.buttonGroup.setId(self.ui.rb6, 6)
        self.ui.buttonGroup_2.setId(self.ui.rb00, 0)
        self.ui.buttonGroup_2.setId(self.ui.rb11, 1)
        self.ui.buttonGroup_2.setId(self.ui.rb22, 2)
        self.ui.buttonGroup_2.setId(self.ui.rb33, 3)
        self.ui.buttonGroup_2.setId(self.ui.rb44, 4)
        self.ui.buttonGroup_2.setId(self.ui.rb55, 5)
        self.ui.buttonGroup_2.setId(self.ui.rb66, 6)
        # General functions
        self.ui.save_chars.clicked.connect(self.upd_char)
        self.ui.save_weap.clicked.connect(self.upd_weap)
        self.ui.tabWidget.currentChanged.connect(lambda: self.transfer(self.ui.tabWidget.currentIndex()))

        self.ui.clear_chars.clicked.connect(lambda: self.clear_buttons('chars', added, actions_chars))
        self.ui.clear_weap.clicked.connect(lambda: self.clear_buttons('weap', added_w, actions_weap))

    # __________________________________________________________________________________________________________________
    def create_actions(self, mode: str, listt: list, category: QtWidgets.QMenu):
        for name in listt:
            namesp = self.name_translate(name, "_", " ")
            name1 = self.name_translate(name, "'", '')
            name2 = self.name_translate(name1, "-", "_")
            curr = QAction()
            curr.setCheckable(True)
            curr.setText(namesp)
            curr.setFont(QFont(self.fontgensh, 9))
            if mode == 'characters':
                curr.triggered.connect(self.add_char_button)
                actions_chars[name] = curr
            elif mode == 'weapon':
                curr.triggered.connect(self.add_weap_button)
                actions_weap[name2] = curr
            category.addAction(curr)
    # __________________________________________________________________________________________________________________

    # __________________________________________________________________________________________________________________
    @staticmethod
    def name_translate(name: str, from_: str, to: str):
        """
        :param name: обрабатываемая строка
        :param from_: символ, который нужно заменить
        :param to: символ, на который нужно заменить
        :return: измененная строка
        """
        if from_ in name:
            return to.join(name.split(from_))
        else:
            return name
    # __________________________________________________________________________________________________________________

    def add_char_button(self):
        sender = self.sender()
        namesp = sender.text()
        nameus = self.name_translate(namesp, ' ', '_')
        if sender.isChecked and nameus not in added.keys():
            # adding a button
            btn = QToolButton(parent=self.ui.scrollAreaChars)
            btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            btn.clicked.connect(self.upd_right_menu_char)
            btn.setText(namesp)
            btn.setFont(QFont(self.fontgensh, 13))
            self.ui.horizontalLayout_6.addWidget(btn)
            # Icon, its Geometry
            btn.setIcon(QtGui.QIcon(f":/chars/all/{nameus}.webp"))
            btn.setIconSize(QtCore.QSize(270, 520))

            added[nameus] = btn
        else:
            nn = added[nameus]
            nn.setParent(None)
            del added[nameus]
            if nameus in chosen.keys():
                del chosen[nameus]
            if not added:
                global currNameChar
                currNameChar = ''

    def upd_char(self):  # for save button
        if not currNameChar:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Click on character's portrait!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        clvl, rlvl = self.ui.spinBoxCCL.value(), self.ui.spinBoxRCL.value()
        casc, rasc = self.ui.buttonGroup_2.checkedId(), self.ui.buttonGroup.checkedId()
        ctal1, rtal1 = self.ui.sliderNormal.value(), self.ui.sliderReqNormal.value()
        ctal2, rtal2 = self.ui.sliderSkill.value(), self.ui.sliderReqSkill.value()
        ctal3, rtal3 = self.ui.sliderBurst.value(), self.ui.sliderReqBurst.value()
        chosen[currNameChar] = Char_info(clvl, rlvl, casc, rasc, ctal1, ctal2, ctal3, rtal1, rtal2, rtal3)

    def upd_right_menu_char(self):
        sender = self.sender()
        bb = sender.text()
        # Receiving char's name from button
        global currNameChar
        currNameChar = self.name_translate(bb, ' ', '_')

        # setting saved info
        if currNameChar in chosen.keys():
            aa = chosen[currNameChar]
            self.ui.spinBoxCCL.setValue(aa.clvl)
            self.ui.spinBoxRCL.setValue(aa.rlvl)
            self.ui.buttonGroup_2.button(aa.casc).click()
            self.ui.buttonGroup.button(aa.rasc).click()
            self.ui.sliderNormal.setValue(aa.ctal1)
            self.ui.sliderSkill.setValue(aa.ctal2)
            self.ui.sliderBurst.setValue(aa.ctal3)
            self.ui.sliderReqNormal.setValue(aa.rtal1)
            self.ui.sliderReqSkill.setValue(aa.rtal2)
            self.ui.sliderReqBurst.setValue(aa.rtal3)
        else:
            self.set_to_default()

    def upd_right_menu_weap(self):
        sender = self.sender()
        bb = sender.text()
        nameus = self.name_translate(bb, ' ', '_')
        name1 = self.name_translate(nameus, "'", '')
        name2 = self.name_translate(name1, "-", "_")
        global currNameWeap
        currNameWeap = name2

        if currNameWeap in chosen_w.keys():
            dd = chosen_w[currNameWeap]
            self.ui.spinBoxWL.setValue(dd.clvl)
            self.ui.spinBoxRWL.setValue(dd.rlvl)
            self.ui.dialRef.setValue(dd.casc)
            self.ui.dialReqRef.setValue(dd.rasc)
        else:
            self.ui.spinBoxWL.setValue(1)
            self.ui.spinBoxRWL.setValue(1)
            self.ui.dialRef.setValue(0)
            self.ui.dialReqRef.setValue(0)

    def add_weap_button(self):
        sender = self.sender()
        namesp = sender.text()
        nameus = self.name_translate(namesp, ' ', '_')
        name1 = self.name_translate(nameus, "'", '')
        name2 = self.name_translate(name1, "-", "_")
        if sender.isChecked() and nameus not in added_w.keys():
            # adding a button
            btn = QToolButton(parent=self.ui.scrollAreaWeap)
            btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            btn.clicked.connect(self.upd_right_menu_weap)
            btn.setText(namesp)
            btn.setFont(QFont(self.fontgensh, 12))
            self.ui.horizontalLayout_7.addWidget(btn)

            # Icon, it's Geometry
            btn.setIcon(QtGui.QIcon(f":/weapon/all/{name2}.webp"))
            btn.setIconSize(QtCore.QSize(220, 220))

            added_w[name2] = btn
        else:
            # deleting button and weapon info
            nn = added_w[name2]
            nn.setParent(None)
            del added_w[name2]
            if name2 in chosen_w.keys():
                del chosen_w[name2]
            if not added_w:
                global currNameWeap
                currNameWeap = ''

    def upd_weap(self):
        if not currNameWeap:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText('Click on weapon image!')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        clvl = self.ui.spinBoxWL.value()
        rlvl = self.ui.spinBoxRWL.value()
        casc = self.ui.dialRef.value()
        rasc = self.ui.dialReqRef.value()
        chosen_w[currNameWeap] = Weap_info(clvl, rlvl, casc, rasc)

    def set_to_default(self):
        self.ui.spinBoxCCL.setValue(0)
        self.ui.spinBoxRCL.setValue(0)
        self.ui.buttonGroup_2.button(0).click()
        self.ui.buttonGroup.button(0).click()
        self.ui.sliderNormal.setValue(1)
        self.ui.sliderSkill.setValue(1)
        self.ui.sliderBurst.setValue(1)
        self.ui.sliderReqNormal.setValue(1)
        self.ui.sliderReqSkill.setValue(1)
        self.ui.sliderReqBurst.setValue(1)
    # __________________________________________________________________________________________________________________

    @staticmethod
    def clear_buttons(mode: str, added_: dict, actions: dict):
        for name, val in added_.items():
            val.setParent(None)
            actions[name].setChecked(False)
        if mode == 'chars':
            global currNameChar, added, chosen
            currNameChar = ''
            added = {}
            chosen = {}
        else:
            global currNameWeap, added_w, chosen_w
            currNameWeap = ''
            added_w = {}
            chosen_w = {}
    # __________________________________________________________________________________________________________________

    @classmethod
    def calc_chars(cls):
        """Calcs resources required for chosen characters"""
        print("----------\nfrom calc_chars")
        global resources
        resources = copy.deepcopy(resources_clear)
        print(list(resources.keys()))
        for name, pers in chosen.items():
            cls.count_tal(pers.ctal1, pers.rtal1, all_chars[name].talent_book.name, books_tals)  # Talent books
            cls.count_tal(pers.ctal2, pers.rtal2, all_chars[name].talent_book.name, books_tals)
            cls.count_tal(pers.ctal3, pers.rtal3, all_chars[name].talent_book.name, books_tals)

            cls.count_tal(pers.ctal1, pers.rtal1, all_chars[name].enemie.name, enemies_tals)     # Talent enemies
            cls.count_tal(pers.ctal2, pers.rtal2, all_chars[name].enemie.name, enemies_tals)
            cls.count_tal(pers.ctal3, pers.rtal3, all_chars[name].enemie.name, enemies_tals)

            for m in range(pers.casc, pers.rasc):
                if m == 0:
                    resources[all_chars[name].gems.name][1] += gems[m]
                    resources[all_chars[name].enemie.name][1] += enemies_asc[m]
                elif m == 1:
                    resources[all_chars[name].gems.name][2] += gems[m]
                    resources[all_chars[name].enemie.name][1] += enemies_asc[m]
                elif m == 2:
                    resources[all_chars[name].gems.name][2] += gems[m]
                    resources[all_chars[name].enemie.name][2] += enemies_asc[m]
                elif m == 3:
                    resources[all_chars[name].gems.name][3] += gems[m]
                    resources[all_chars[name].enemie.name][2] += enemies_asc[m]
                elif m == 4:
                    resources[all_chars[name].gems.name][3] += gems[m]
                    resources[all_chars[name].enemie.name][3] += enemies_asc[m]
                elif m == 5:
                    resources[all_chars[name].gems.name][4] += gems[m]
                    resources[all_chars[name].enemie.name][3] += enemies_asc[m]

            resources['total_mora'] += sum(mora_asc[pers.casc:pers.rasc]) + sum(mora_tals[pers.ctal1:pers.rtal1])
            resources["total_mora"] += sum(mora_tals[pers.ctal2:pers.rtal2]) + sum(mora_tals[pers.ctal3:pers.rtal3])

            resources[all_chars[name].local.name] += sum(local[pers.casc:pers.rasc])
            resources[all_chars[name].boss.name] += sum(boss[pers.casc:pers.rasc])
            resources[all_chars[name].boss_tal.name] += sum(boss_tals[pers.ctal1:pers.rtal1])
            resources[all_chars[name].boss_tal.name] += sum(boss_tals[pers.ctal2:pers.rtal2])
            resources[all_chars[name].boss_tal.name] += sum(boss_tals[pers.ctal3:pers.rtal3])

            resources['total_exp'] += sum(exp_lvl[pers.clvl:pers.rlvl])  # Experience

        resources["book_exp"][3] += resources['total_exp'] // 20_000
        resources['total_mora'] += 4000 * (resources['total_exp'] // 20_000)
        resources['total_exp'] %= 20_000
        resources["book_exp"][2] += resources['total_exp'] // 5000
        resources['total_mora'] += 1000 * (resources['total_exp'] // 5000)
        resources['total_exp'] %= 5000
        resources["book_exp"][1] += resources['total_exp'] // 1000
        resources['total_mora'] += 200 * (resources['total_exp'] // 1000)
        resources['total_exp'] %= 1000

        if resources['total_exp'] != 0:
            resources["book_exp"][1] += 1
            resources['total_mora'] += 200
        resources['total_exp'] = 0

        print('resources\n', resources, '\n-------------')

    @classmethod
    def calc_weap(cls):
        print('-----------\nfrom calc_weap')
        global resources
        print(chosen_w.keys(), "\n", all_weap.keys())
        for name, weap in chosen_w.items():
            if all_weap[name].rarity == 4:
                resources['total_mora'] += sum(mora_asc_w4[weap.casc:weap.rasc])
                for a in range(weap.casc, weap.rasc):
                    if a == 0:
                        resources[all_weap[name].asc.name][1] += dange4[a]
                        resources[all_weap[name].enemie_gen.name][1] += enemies_gen4[a]
                        resources[all_weap[name].enemie_elite.name][1] += enemies_elite4[a]
                    elif a == 1:
                        resources[all_weap[name].asc.name][2] += dange4[a]
                        resources[all_weap[name].enemie_gen.name][1] += enemies_gen4[a]
                        resources[all_weap[name].enemie_elite.name][1] += enemies_elite4[a]
                    elif a == 2:
                        resources[all_weap[name].asc.name][2] += dange4[a]
                        resources[all_weap[name].enemie_gen.name][2] += enemies_gen4[a]
                        resources[all_weap[name].enemie_elite.name][2] += enemies_elite4[a]
                    elif a == 3:
                        resources[all_weap[name].asc.name][3] += dange4[a]
                        resources[all_weap[name].enemie_gen.name][2] += enemies_gen4[a]
                        resources[all_weap[name].enemie_elite.name][2] += enemies_elite4[a]
                    elif a == 4:
                        resources[all_weap[name].asc.name][3] += dange4[a]
                        resources[all_weap[name].enemie_gen.name][3] += enemies_gen4[a]
                        resources[all_weap[name].enemie_elite.name][3] += enemies_elite4[a]
                    elif a == 5:
                        resources[all_weap[name].asc.name][4] += dange4[a]
                        resources[all_weap[name].enemie_gen.name][3] += enemies_gen4[a]
                        resources[all_weap[name].enemie_elite.name][3] += enemies_elite4[a]
            else:
                for a in range(weap.casc, weap.rasc):
                    resources['total_mora'] += sum(mora_asc_w5[weap.casc:weap.rasc])
                    if a == 0:
                        resources[all_weap[name].asc.name][1] += dange5[a]
                        resources[all_weap[name].enemie_gen.name][1] += enemies_gen5[a]
                        resources[all_weap[name].enemie_elite.name][1] += enemies_elite5[a]
                    elif a == 1:
                        resources[all_weap[name].asc.name][2] += dange5[a]
                        resources[all_weap[name].enemie_gen.name][1] += enemies_gen5[a]
                        resources[all_weap[name].enemie_elite.name][1] += enemies_elite5[a]
                    elif a == 2:
                        resources[all_weap[name].asc.name][2] += dange5[a]
                        resources[all_weap[name].enemie_gen.name][2] += enemies_gen5[a]
                        resources[all_weap[name].enemie_elite.name][2] += enemies_elite5[a]
                    elif a == 3:
                        resources[all_weap[name].asc.name][3] += dange5[a]
                        resources[all_weap[name].enemie_gen.name][2] += enemies_gen5[a]
                        resources[all_weap[name].enemie_elite.name][2] += enemies_elite5[a]
                    elif a == 4:
                        resources[all_weap[name].asc.name][3] += dange5[a]
                        resources[all_weap[name].enemie_gen.name][3] += enemies_gen5[a]
                        resources[all_weap[name].enemie_elite.name][3] += enemies_elite5[a]
                    elif a == 5:
                        resources[all_weap[name].asc.name][4] += dange5[a]
                        resources[all_weap[name].enemie_gen.name][3] += enemies_gen5[a]
                        resources[all_weap[name].enemie_elite.name][3] += enemies_elite5[a]

            resources['exp_weapon'] += sum(exp_weap[weap.clvl:weap.rlvl])

            resources["crystal_exp"][3] += resources['exp_weapon'] // 10_000
            resources['total_mora'] += 1000 * (resources['exp_weapon'] // 10_000)
            resources['exp_weapon'] %= 10_000
            resources["crystal_exp"][2] += resources['exp_weapon'] // 2000
            resources['total_mora'] += 200 * (resources['exp_weapon'] // 2000)
            resources['exp_weapon'] %= 2000
            resources["crystal_exp"][1] += resources['exp_weapon'] // 400
            resources['total_mora'] += 40 * (resources['exp_weapon'] // 400)
            resources['exp_weapon'] %= 400

            if resources['exp_weapon'] != 0:
                resources['crystal_exp'][1] += 1
                resources['total_mora'] += 40
            resources['exp_weapon'] = 0

    @staticmethod
    def count_tal(c: int, r: int, name: str, array: tuple):
        global resources
        for h in range(c, r):
            if h == 1:
                resources[name][1] += array[h]
            elif h in [2, 3, 4, 5]:
                resources[name][2] += array[h]
            elif h in [6, 7, 8, 9]:
                resources[name][3] += array[h]

    @staticmethod
    def clear_layout(layout: QFormLayout, rest: int = 0):
        while layout.rowCount() > rest:  # deleting previous rows
            layout.removeRow(layout.rowCount() - 1)

    def transfer(self, idx: int):
        self.calc_chars()
        self.calc_weap()
        if idx == 1:
            self.print_results()
        elif idx == 2:
            self.add_inventory_line()
            self.add_permanent_rows(mode=1)

    def print_results(self):
        print('from print_results')
        print('resources\n', resources)

        for lll in [self.ui.formLayout, self.ui.formLayout_2, self.ui.formLayout_3, self.ui.formLayout_4]:
            self.clear_layout(lll)

        for name, r in resources.items():
            if name == 'total_mora' or name in list(Enemies_gen.__members__.keys()):
                lay = self.ui.formLayout
            elif (name == 'book_exp' or name in list(Locals.__members__.keys()) or
                  name in list(Boss.__members__.keys()) or name in list(Gems.__members__.keys())):
                lay = self.ui.formLayout_4
            elif name in list(Talents.__members__.keys()) or name in list(Boss_tals.__members__.keys()):
                lay = self.ui.formLayout_3
            else:
                lay = self.ui.formLayout_2

            if isinstance(r, list):  # list resources - enemies loot, etc.
                if name in list(Asc_weap.__members__.keys()) or name in list(Gems.__members__.keys()):
                    smth = 5
                else:
                    smth = 4
                for i in range(0, smth):
                    if r[i] == 0:
                        continue
                    label = QLabel()
                    label2 = QLabel()
                    label2.setText(str(r[i]))
                    label2.setFont(QFont(self.fontgensh, 20))
                    pic = QtGui.QPixmap(f":/resources/all/{name + str(i)}.webp")
                    pic = pic.scaled(170, 170, transformMode=Qt.SmoothTransformation)
                    label.setPixmap(pic)
                    lay.addRow(label, label2)
            else:
                if r == 0:
                    continue
                label = QLabel()
                label2 = QLabel()
                pic = QtGui.QPixmap(f":/resources/all/{name}.webp")
                pic = pic.scaled(170, 170, transformMode=Qt.SmoothTransformation)
                label.setPixmap(pic)
                label2.setText(str(r))
                label2.setFont(QFont(self.fontgensh, 20))
                lay.addRow(label, label2)
        print('-------------')

    def add_permanent_rows(self, mode: int = 0):
        font = QtGui.QFont(self.fontgensh, 15, 75)
        font.setBold(True)

        label = QLabel("Enter your inventory contents")
        btn = QPushButton(text="Calculate")
        label.setFont(font)
        btn.setFont(font)
        btn.clicked.connect(self.calc_inventory)
        btn.setFixedSize(150, 50)
        self.ui.formLayout_7.addRow(label, btn)

        if mode:
            return

        label1 = QLabel("Choose transforming mode")
        label1.setFont(font)
        lay = QHBoxLayout()
        lay.setSpacing(20)

        font1 = QtGui.QFont(self.fontgensh, 15)
        rbtn1 = QRadioButton(text="More rare first")
        rbtn1.setFont(font1)

        rbtn2 = QRadioButton(text="More common first")
        rbtn2.setFont(font1)
        self.ButtonGroupTransform = QButtonGroup()
        self.ButtonGroupTransform.addButton(rbtn1, 1)
        self.ButtonGroupTransform.addButton(rbtn2, 2)
        rbtn1.setChecked(True)
        lay.addWidget(rbtn1)
        lay.addWidget(rbtn2)
        self.ui.formLayout_7.addRow(label1, lay)

    def for_clear_btn(self):
        button = self.sender()

        # looking for the same button to get its name
        for name, val in cont.items():
            if len(val) < 3:
                continue
            b2 = val[2]
            if id(button) == id(b2):
                nn = list(name)
                nn.pop()
                currname = ''.join(nn)
                break
        # setting to zero all spinboxes in this resources group
        for i in range(5):
            if currname + str(i) not in cont.keys():
                continue
            cont[currname + str(i)][0].setValue(0)

    def add_inventory_line(self):
        print('------------\nfrom add_inventory_line\n', cont.keys())
        self.clear_layout(self.ui.formLayout_7, rest=2)
        font = QtGui.QFont(self.fontgensh, 12)
        print('resources1\n', resources)
        print('having1\n', having)
        prevname = ""
        for name, val in resources.items():
            print(name)
            if name in ['total_exp', 'exp_weapon']:
                continue
            if isinstance(val, list):
                if name in list(Asc_weap.__members__.keys()) or name in list(Gems.__members__.keys()):
                    smth = 5
                else:
                    smth = 4
                flag = False
                for i in range(smth):
                    if val[i] == 0:
                        continue
                    label = QLabel()
                    pic = QtGui.QPixmap(f":/resources/all/{name + str(i)}.webp")
                    pic = pic.scaled(170, 170, transformMode=Qt.SmoothTransformation)
                    label.setPixmap(pic)
                    ver = QVBoxLayout()

                    spin = QSpinBox()
                    spin.setFont(font)
                    spin.setMaximum(500000000)
                    ver.addWidget(spin)

                    label1 = QLabel()
                    label1.setFont(font)

                    if name in having:
                        spin.setValue(having[name][i])
                        if resources[name][i] - having[name][i] <= 0:
                            label1.setText('You have enough')
                        else:
                            label1.setText(f"You need {resources[name][i] - having[name][i]}  more")

                    cont[name + str(i)] = [spin, label1]

                    if name != prevname and not flag:
                        button = QPushButton(text="Clear")
                        button.clicked.connect(self.for_clear_btn)
                        button.setFont(font)
                        ver.addWidget(button)
                        flag = True
                        cont[name + str(i)].append(button)

                    ver.addWidget(label1)
                    self.ui.formLayout_7.addRow(label, ver)
            else:
                if val == 0:
                    continue
                label = QLabel()
                pic = QtGui.QPixmap(f":/resources/all/{name}.webp")
                pic = pic.scaled(170, 170, transformMode=Qt.SmoothTransformation)
                label.setPixmap(pic)
                ver = QVBoxLayout()
                spin = QSpinBox()
                label1 = QLabel()
                spin.setFont(font)
                label1.setFont(font)
                spin.setMaximum(500000000)
                ver.addWidget(spin)
                ver.addWidget(label1)

                if name in having:
                    spin.setValue(having[name])
                    if resources[name] - having[name] <= 0:
                        label1.setText('You have enough')
                    else:
                        label1.setText(f"You need {resources[name] - having[name]} more")

                cont[name] = [spin, label1]
                self.ui.formLayout_7.addRow(label, ver)
            prevname = name

    @staticmethod
    def receive_inv():
        print('-------------\nfrom receive_inv')
        global having
        having = copy.deepcopy(resources)
        print('cont\n', cont, "having\n", having)

        for name, val in having.items():
            if name in ['total_exp', 'exp_weapon']:
                continue
            if isinstance(val, int) and name in cont.keys():
                having[name] = cont[name][0].value()
            elif isinstance(val, list):
                if name in list(Asc_weap.__members__.keys()) or name in list(Gems.__members__.keys()):
                    smth = 5
                else:
                    smth = 4
                for i in range(smth):
                    if name + str(i) in cont.keys():
                        having[name][i] = cont[name + str(i)][0].value()
        print('having after\n', having)
        print('resources\n', resources)
        print('----------')

    def calc_inventory(self):
        self.receive_inv()
        if self.ButtonGroupTransform.checkedId() == 1:
            self.transform()
        else:
            self.reversed_transform()
        global cont
        print('from calc_inventory')
        print('transformed having\n', having)
        for name, val in having.items():
            if name in ['total_exp', 'exp_weapon']:
                continue
            if isinstance(val, int) and name in cont.keys():
                if resources[name] - val <= 0:
                    cont[name][1].setText('You have enough')
                else:
                    cont[name][1].setText(f"You need {resources[name] - val} more")
            elif isinstance(val, list):
                if name in list(Asc_weap.__members__.keys()) or name in list(Gems.__members__.keys()):
                    smth = 5
                else:
                    smth = 4
                for i in range(0, smth):
                    nn = ''.join([name, str(i)])
                    if nn in cont.keys():
                        if resources[name][i] - val[i] <= 0:
                            cont[nn][1].setText('You have enough')
                        else:
                            cont[nn][1].setText(f"You need {resources[name][i] - val[i]} more")
        print('------------')

    @staticmethod
    def transform():
        print('-----------------\n from transform')
        global having
        global cont
        entered = copy.deepcopy(having)
        for name, val in having.items():
            if isinstance(val, int):
                continue
            if name in list(Asc_weap.__members__.keys()) or name in list(Gems.__members__.keys()):
                smth = 5
            else:
                smth = 4
            for i in range(smth - 1):
                if resources[name][i + 1] == 0:
                    break
                if val[i] >= 3:
                    having[name][i + 1] += val[i] // 3
                    having[name][i] = val[i] % 3
            print(name, 'one-side transformed having\n', having)
            for i in range(smth - 1, 1, -1):
                if resources[name][i - 1] == 0:
                    break
                if having[name][i] > resources[name][i]:
                    having[name][i - 1] += 3 * (having[name][i] - resources[name][i])
                    having[name][i] -= (having[name][i] - resources[name][i])
            print('two-side transformed having\n', having)
            print('entered\n', entered)
            print('cont keys\n', cont.keys())
            for i in range(smth - 1):
                while having[name][i] > entered[name][i] and \
                        having[name][i] > resources[name][i] and having[name][i] >= 3:
                    having[name][i] -= 3
                    having[name][i + 1] += 1
                if name + str(i) in cont.keys():
                    cont[name + str(i)][0].setValue(having[name][i])
                if name + str(i + 1) in cont.keys():
                    cont[name + str(i + 1)][0].setValue(having[name][i + 1])

        print('three-side transformed having\n', having, '\n--------------')

    @staticmethod
    def reversed_transform():
        print('---------------\nfrom reversed_transform')
        global having
        global cont
        orighaving = copy.deepcopy(having)
        for name, val in having.items():
            if isinstance(val, int):
                continue
            if name in list(Asc_weap.__members__.keys()) or name in list(Gems.__members__.keys()):
                smth = 5
            else:
                smth = 4
            for i in range(smth - 1):  # one side  * -> ** -> *** -> ****
                if having[name][i] <= resources[name][i]:
                    continue
                if resources[name][i + 1] == 0:
                    break
                rest = having[name][i] - resources[name][i]
                having[name][i] -= rest
                having[name][i + 1] += rest // 3
                having[name][i] += rest % 3
                print(name, i, "having1\n", having)
                if name + str(i) in cont.keys():
                    cont[name + str(i)][0].setValue(having[name][i])
                if name + str(i + 1) in cont.keys():
                    cont[name + str(i + 1)][0].setValue(having[name][i + 1])

            for i in range(smth - 1, 1, -1):
                if resources[name][i - 1] == 0 or orighaving[name][i]>=having[name][i]:
                    break
                if having[name][i] > resources[name][i]:
                    rest = having[name][i] - resources[name][i]
                    having[name][i] -= rest
                    having[name][i - 1] += rest * 3
                    if name + str(i) in cont.keys():
                        cont[name + str(i)][0].setValue(having[name][i])
                    if name + str(i - 1) in cont.keys():
                        cont[name + str(i - 1)][0].setValue(having[name][i - 1])
                print(name, i, "having2\n", having)
        print('-------------------')


def read_file(mode: str, file: str, chosen_: dict, actions: dict):
    try:
        with open(file, "r") as file_:
            for line in file_:
                curr = line.split()
                name = curr[0]
                del curr[0]
                curr1 = list(map(int, curr))
                if mode == 'chars':
                    chosen_[name] = Char_info(*curr1)
                else:
                    chosen_[name] = Weap_info(*curr1)
                actions[name].trigger()
    except FileNotFoundError:
        pass


@atexit.register
def write_file_chars():
    with open("saves_chars.txt", 'w') as file_chars:
        for name, val in chosen.items():
            file_chars.write(
                f"{name} {val.clvl} {val.rlvl} {val.casc} {val.rasc} "
                f"{val.ctal1} {val.ctal2} {val.ctal3} {val.rtal1} {val.rtal2} {val.rtal3}\n"
            )


@atexit.register
def write_file_weap():
    with open("saves_weap.txt", 'w') as file_weap:
        for name, val in chosen_w.items():
            file_weap.write(f"{name} {val.clvl} {val.rlvl} {val.casc} {val.rasc}\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('Diffnes.qss', 'r') as qss:
        app.setStyleSheet(qss.read())
    window = Window()
    window.show()
    read_file('chars', "saves_chars.txt", chosen, actions_chars)
    read_file('weap', "saves_weap.txt", chosen_w, actions_weap)
    sys.exit(app.exec_())
