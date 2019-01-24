import sys, time, os, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import tkinter
from tkinter import messagebox

# проба
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initui()
# проба gjkhjkldfghjdfk

    def initui(self):
        self.blok = 0
        self.setGeometry(300, 100, 672, 672)
        self.setWindowTitle('Подземелье')



        self.timer = QBasicTimer()
        self.spisoc = []
        self.sp_bot = []
        self.xp_max = 1000
        self.xp_normal = 1000
        self.mp_max = 100
        self.mp_normal = 100
        self.animachiyakasta = 0
        self.god = 0
        self.manp = 0
        self.pq = ''
        self.st_time = 0
        self.gobl_killed = 10
        self.spisoc_31 = []
        self.spisoc_32 = []
        self.spisoc_33 = []
        self.spisoc_34 = []

        with open('pic/map.txt', 'r') as f:
            for i in range(222):
                a = f.readline()
                self.spisoc.append(list(map(int, a.split())))

        with open('pic/map_gobl.txt', 'r') as f:
            for i in range(222):
                a = f.readline()
                self.sp_bot.append(list(map(int, a.split())))

        self.x = 27
        self.y = 207

        self.pixmap = [QPixmap('pic/1.png'), QPixmap('pic/2.png'), QPixmap('pic/3.png'), QPixmap('pic/4.png'), QPixmap('pic/5.png'),
                       QPixmap('pic/6.png'), QPixmap('pic/7.png'), QPixmap('pic/8.png'), QPixmap('pic/9.png'),QPixmap('pic/10.png'),
                       QPixmap('pic/11.png'), QPixmap('pic/12.png'), QPixmap('pic/13.png'), QPixmap('pic/14.png'), QPixmap('pic/15.png'),
                       QPixmap('pic/16.png'), QPixmap('pic/17.png'), QPixmap('pic/18.png'), QPixmap('pic/19.png'), QPixmap('pic/20.png'),
                       QPixmap('pic/21.png'), QPixmap('pic/22.png'), QPixmap('pic/23.png'), QPixmap('pic/24.png'), QPixmap('pic/25.png'),
                       QPixmap('pic/26.png'), QPixmap('pic/27.png'), QPixmap('pic/28.png'), QPixmap('pic/29.png'),
                       QPixmap('pic/30.png'), QPixmap('pic/31.png'), QPixmap('pic/32.png'), QPixmap('pic/33.png'), QPixmap('pic/34.png')]

        self.go = [QPixmap('pic/gl.png'), QPixmap('pic/gz.png'), QPixmap('pic/gp.png'), QPixmap('pic/gs.png'), QPixmap('pic/gm1.png'),
                   QPixmap('pic/gm2.png'), QPixmap('space.png')]
        self.fb_pix = [QPixmap('pic/al.png'), QPixmap('pic/av.png'), QPixmap('pic/ap.png'), QPixmap('pic/an.png'), QPixmap('pic/space.png')]

        self.n = 3

        self.p = []
        for i in range(7):
            self.p.append([])
            for j in range(7):
                self.p[i].append(QLabel(self))
                self.p[i][j].move(j*96, i*96)

        for i in range(7):
            for j in range(7):
                n=self.spisoc[self.y + i - 3][self.x + j - 3]-1
                self.p[i][j].setPixmap(self.pixmap[n])

        self.pi = [QPixmap('pic/igrml_.png'), QPixmap('pic/igrmz_.png'), QPixmap('pic/igrmp_.png'), QPixmap('pic/igrms_.png'), QPixmap('pic/igrml_mg.png')]
        self.kast = [QPixmap('pic/igrml_a.png'), QPixmap('pic/igrmz_a.png'), QPixmap('pic/igrmp_a.png'), QPixmap('pic/igrms_a.png')]
        self.pw = QLabel(self)
        p = self.pi[3].copy()
        self.pp = QPainter(p)
        self.pp.setPen(QColor(255, 0, 0))
        self.pp.drawRect(23, 0, 40, 3)
        self.pp.setPen(QColor(0, 0, 255))
        self.pp.drawRect(23, 5, 40, 3)
        self.pp.fillRect(23, 0, int(40 * (self.xp_normal / self.xp_max)), 3, QColor(255, 0, 0))
        self.pp.fillRect(23, 5, int(40 * (self.mp_normal / self.mp_max)), 3, QColor(0, 0, 255))
        self.pp.end()
        self.pw.setPixmap(p)
        self.pw.move(288, 288)

        for i in range(len(self.spisoc)):
            for j in range(len(self.spisoc[0])):
                if self.spisoc[i][j] == 31:
                    self.spisoc_31.append([i, j])
        for i in range(len(self.spisoc)):
            for j in range(len(self.spisoc[0])):
                if self.spisoc[i][j] == 32:
                    self.spisoc_32.append([i, j])
        for i in range(len(self.spisoc)):
            for j in range(len(self.spisoc[0])):
                if self.spisoc[i][j] == 33:
                    self.spisoc_33.append([i, j])
        for i in range(len(self.spisoc)):
            for j in range(len(self.spisoc[0])):
                if self.spisoc[i][j] == 34:
                    self.spisoc_34.append([i, j])

        self.gobls = []
        self.gobls_xp = []
        self.gobls_pw = []
        for i in range(len(self.sp_bot)):
            for j in range(len(self.sp_bot[0])):
                if self.sp_bot[i][j] > 32768:
                    # тип монстров
                    tm = (self.sp_bot[i][j] - 32768) // 256
                    # колличество монстров
                    km = self.sp_bot[i][j] % 256
                    if tm == 0:
                        for k in range(km):
                            self.gobls.append(goblin(j, i))
                            self.gobls_xp.append(20)
                            self.gobls_pw.append(QLabel(self))
                    if tm == 1:
                        self.gobls.append(goblin(j, i))
                        self.gobls_xp.append(20)
                        self.gobls_pw.append(QLabel(self))
        self.fb = []
        self.fb_pw = []
        for k in range(10):
            self.fb.append(fireboll())
            self.fb_pw.append(QLabel(self))

        for i in range(len(self.gobls_pw)):
            self.gobls_pw[i].setPixmap(self.go[3])
            gx, gy, gn, xp = self.gobls[i].getcoord()
            self.gobls_pw[i].move((gx - self.x + 3) * 96, (gy - self.y + 3) * 96)

        for i in range(10):
            self.fb_pw[i].setPixmap(self.fb_pix[0])
            gx, gy, gn = self.fb[i].getcoord()
            self.fb_pw[i].move((gx - self.x + 3) * 96, (gy - self.y + 3) * 96)
        self.sdfg = QPixmap('pic/zast.png')
        self.zastavka = QLabel(self)
        self.zastavka.setPixmap(self.sdfg)
        self.na()
        self.show()

# nnnhjgh
    def na(self):
        self.game = QPushButton(self)
        self.game.move(236, 236)
        self.game.resize(200, 200)
        self.game.setText("НАЧАТЬ ИГРУ")
        self.game.clicked.connect(self.clas)


    def clas(self):
        if self.sender() == self.game:
            self.game.deleteLater()
            self.blok = 1
            self.zastavka.move(1000, 1000)



    def keyPressEvent(self, event):
        if self.mp_max > self.mp_normal:
            self.mp_normal += 2
        if self.xp_max > self.xp_normal:
            self.xp_normal += 3
        if self.god == 1:
            if self.mp_max > self.mp_normal+50:
                self.mp_normal += 50
            if self.xp_max > self.xp_normal+500:
                self.xp_normal += 500
            if event.key() == Qt.Key_F:
                if self.spisoc[self.y - 1][self.x] == 34:
                    self.spisoc[self.y - 1][self.x] = 0
                self.spisoc[self.y - 1][self.x] += 1
            if event.key() == Qt.Key_W:
                with open('pic/map.txt', 'w') as t:
                    for i in self.spisoc:
                        t.write(' '.join(list(map(str, i))) + '\n')
        if event.key() == Qt.Key_0:
            if self.god == 1:
                self.god = 0
            else:
                self.god = 1
            print('1')
        if self.blok:
            if self.n < 4:
                if event.key() == Qt.Key_Up:
                    self.n = 1
                    self.animachiyakasta = 0
                if event.key() == Qt.Key_Down:
                    self.n = 3
                    self.animachiyakasta = 0
                if event.key() == Qt.Key_Left:
                    self.n = 0
                    self.animachiyakasta = 0
                if event.key() == Qt.Key_Right:
                    self.n = 2
                    self.animachiyakasta = 0

                if event.key() == Qt.Key_Shift:
                    sn = [(self.y, self.x - 1), (self.y - 1, self.x), (self.y, self.x + 1), (self.y + 1, self.x)]
                    y01, x01 = sn[self.n]
                    if (self.sp_bot[y01][x01] >= 1 and self.sp_bot[y01][x01] <= 9) or self.god == 1:
                        self.y, self.x = sn[self.n]
                    self.animachiyakasta = 0
            else:
                root = tkinter.Tk()
                root.withdraw()
                i = 0
                for j in range(len(self.gobls)):
                    xg, yg, ng, xp = self.gobls[j].getcoord()
                    if ng >= 4:
                        i += 1
                ret = messagebox.askyesno("Вы погибли", 'Вы ценой своей жизни убили '+str(i)+' гоблинов\n'+'осталось '
                                          + str(len(self.gobls) - i + 1)+'\n'+"Начать сначала?")
                if not ret:
                    exit()
                else:
                    self.x = 27
                    self.y = 206
                    self.n = 3
                    sho = 0
                    self.xp_max = 1000
                    self.xp_normal = 1000
                    self.mp_max = 100
                    self.mp_normal = 100
                    self.manp = 0




            # Рисуем текстуры
            for i in range(7):
                for j in range(7):
                    n = self.spisoc[self.y + i - 3][self.x + j - 3] - 1
                    if n == 23:
                        if self.gobl_killed >= 8:
                            n = 24
                        if self.gobl_killed >= 16:
                            n = 25
                    self.p[i][j].setPixmap(self.pixmap[n])


            # Рисуем человека
            self.pq = self.pi[self.n].copy()
            self.pp = QPainter(self.pq)
            self.pp.setPen(QColor(255, 0, 0))
            self.pp.drawRect(23, 0, 40, 3)
            self.pp.setPen(QColor(0, 0, 255))
            self.pp.drawRect(23, 5, 40, 3)
            self.pp.fillRect(23, 0, int(40 * (self.xp_normal / self.xp_max)), 3, QColor(255, 0, 0))
            self.pp.fillRect(23, 5, int(40 * (self.mp_normal / self.mp_max)), 3, QColor(0, 0, 255))
            self.pp.end()
            self.pw.setPixmap(self.pq)

            #self.pw.setPixmap(self.pi[self.n])
            if event.key() == Qt.Key_Space:
                if self.animachiyakasta == 1:
                    self.animachiyakasta = 0
                    for i in range(10):
                        x, y, n = self.fb[i].getcoord()
                        if n == 4:
                            self.fb[i].setcoord(self.x, self.y, self.n)
                            break
                else:
                    if self.mp_normal >= 20:
                        self.mp_normal -= 20
                        self.animachiyakasta = 1
                        self.pq = self.kast[self.n].copy()
                        self.pp = QPainter(self.pq)
                        self.pp.setPen(QColor(255, 0, 0))
                        self.pp.drawRect(23, 0, 40, 3)
                        self.pp.setPen(QColor(0, 0, 255))
                        self.pp.drawRect(23, 5, 40, 3)
                        self.pp.fillRect(23, 0, int(40 * (self.xp_normal / self.xp_max)), 3, QColor(255, 0, 0))
                        self.pp.fillRect(23, 5, int(40 * (self.mp_normal / self.mp_max)), 3, QColor(0, 0, 255))
                        self.pp.end()
                        self.pw.setPixmap(self.pq)
                        #self.pw.setPixmap(self.kast[self.n])

            self.mp_max = 100 + 10 * self.manp
            self.xp_max = 1000 + 10 * self.manp
            d = 0
            for j in range(len(self.gobls)):
                xg, yg, ng, xp = self.gobls[j].getcoord()
                if ng == 7:
                    d += 1
            if d >= 10 + 10 * self.manp:
                self.manp += 1


            for i in range(7):
                for j in range(7):
                    n = self.spisoc[self.y][self.x]
                    if n == 7:
                        root = tkinter.Tk()
                        root.withdraw()
                        i = 0
                        for j in range(len(self.gobls)):
                            xg, yg, ng, xp = self.gobls[j].getcoord()
                            if ng >= 4:
                                i += 1
                        ret = messagebox.askyesno("Вы прошли подземелье!",
                                                  'Вы отважно убили ' + str(i) + ' гоблинов\n' + 'осталось '
                                                  + str(len(self.gobls) - i) + '\n' + "Начать сначала?")
                        if not ret:
                            exit()
                        else:
                            self.x = 27
                            self.y = 206
                            self.n = 3
                            sho = 0
                            self.xp_max = 1000
                            self.xp_normal = 1000
                            self.mp_max = 100
                            self.mp_normal = 100
                            self.manp = 0
                for i in range(7):
                    for j in range(7):
                        n = self.spisoc[self.y][self.x]
                        if n == 6:
                            root = tkinter.Tk()
                            root.withdraw()
                            i = 0
                            for j in range(len(self.gobls)):
                                xg, yg, ng, xp = self.gobls[j].getcoord()
                                if ng >= 4:
                                    i += 1
                            ret = messagebox.askyesno("Вы сбежали ...", "Начать сначала?")
                            if not ret:
                                exit()
                            else:
                                self.x = 27
                                self.y = 206
                                self.n = 3
                                sho = 0
                                self.xp_max = 1000
                                self.xp_normal = 1000
                                self.mp_max = 100
                                self.mp_normal = 100
                                self.manp = 0

            for i in range(10):
                self.fb[i].step(self.sp_bot)

            for i in range(10):
                x, y, n = self.fb[i].getcoord()
                if n < 4:
                    for j in range(len(self.gobls)):
                        xg, yg, ng, xp = self.gobls[j].getcoord()
                        if ng < 4:
                            if x == xg and y == yg:
                                self.fb[i].setcoord(xg, yg, 4)
                                self.gobls[j].kick(self.sp_bot, n, 150)

            for i in range(len(self.gobls)):
                self.gobls[i].step(self.sp_bot, self.x, self.y)

            for i in range(10):
                x, y, n = self.fb[i].getcoord()
                if n < 4:
                    for j in range(len(self.gobls)):
                        xg, yg, ng, xp = self.gobls[j].getcoord()
                        if ng < 4:
                            if x == xg and y == yg:
                                self.fb[i].setcoord(xg, yg, 4)
                                self.gobls[j].kick(self.sp_bot, n, 150)

            xpp = self.xp_normal
            for j in range(len(self.gobls)):
                damag = self.gobls[j].getdamage()
                if damag > 0:
                    self.xp_normal -= damag
                    if self.xp_normal <= 0:
                        self.xp_normal = 0
                        self.n = 4
                        self.pq = self.pi[self.n].copy()
                        self.pp = QPainter(self.pq)
                        self.pp.setPen(QColor(255, 0, 0))
                        self.pp.drawRect(23, 0, 40, 3)
                        self.pp.setPen(QColor(0, 0, 255))
                        self.pp.drawRect(23, 5, 40, 3)
                        self.pp.fillRect(23, 0, int(40 * (self.xp_normal / self.xp_max)), 3, QColor(255, 0, 0))
                        self.pp.fillRect(23, 5, int(40 * (self.mp_normal / self.mp_max)), 3, QColor(0, 0, 255))
                        self.pp.end()
                        self.pw.setPixmap(self.pq)
                        break
            if xpp != self.xp_normal and self.xp_normal != 0:
                self.st_time = 0
                self.pw.setPixmap(self.fb_pix[-1])
                self.timer.start(70, self)

            if self.spisoc[self.y][self.x] == 20:
                self.spisoc[self.y][self.x] = 21
                self.p[3][3].setPixmap(self.pixmap[20])

            if self.spisoc[self.y][self.x] == 24 and self.gobl_killed >= 16:
                self.gobl_killed = 0
                self.xp_max += int(self.xp_max * 0.1)
                self.mp_max += int(self.xp_max * 0.1)
                self.p[3][3].setPixmap(self.pixmap[26])
                self.pq = self.pi[self.n].copy()
                self.pp = QPainter(self.pq)
                self.pp.setPen(QColor(255, 0, 0))
                self.pp.drawRect(23, 0, 40, 3)
                self.pp.setPen(QColor(0, 0, 255))
                self.pp.drawRect(23, 5, 40, 3)
                self.pp.fillRect(23, 0, int(40 * (self.xp_normal / self.xp_max)), 3, QColor(255, 0, 0))
                self.pp.fillRect(23, 5, int(40 * (self.mp_normal / self.mp_max)), 3, QColor(0, 0, 255))
                self.pp.end()

            if self.spisoc[self.y][self.x] == 28:
                self.st_time = 3
                self.timer.start(90, self)
                self.p[3][3].setPixmap(self.pixmap[27])
                self.xp_normal -= 900
                if self.xp_normal <= 0:
                    self.xp_normal = 0
                    self.n = 4
                self.pq = self.pi[self.n].copy()
                self.pp = QPainter(self.pq)
                self.pp.setPen(QColor(255, 0, 0))
                self.pp.drawRect(23, 0, 40, 3)
                self.pp.setPen(QColor(0, 0, 255))
                self.pp.drawRect(23, 5, 40, 3)
                self.pp.fillRect(23, 0, int(40 * (self.xp_normal / self.xp_max)), 3, QColor(255, 0, 0))
                self.pp.fillRect(23, 5, int(40 * (self.mp_normal / self.mp_max)), 3, QColor(0, 0, 255))

            if self.spisoc[self.y][self.x] == 31:
                self.y, self.x = random.choice(self.spisoc_31)
                for i in range(7):
                    for j in range(7):
                        n = self.spisoc[self.y + i - 3][self.x + j - 3] - 1
                        if n == 23:
                            if self.gobl_killed >= 8:
                                n = 24
                            if self.gobl_killed >= 16:
                                n = 25
                        self.p[i][j].setPixmap(self.pixmap[n])

            if self.spisoc[self.y][self.x] == 32:
                self.y, self.x = random.choice(self.spisoc_32)
                for i in range(7):
                    for j in range(7):
                        n = self.spisoc[self.y + i - 3][self.x + j - 3] - 1
                        if n == 23:
                            if self.gobl_killed >= 8:
                                n = 24
                            if self.gobl_killed >= 16:
                                n = 25
                        self.p[i][j].setPixmap(self.pixmap[n])

            if self.spisoc[self.y][self.x] == 33:
                self.y, self.x = random.choice(self.spisoc_33)
                for i in range(7):
                    for j in range(7):
                        n = self.spisoc[self.y + i - 3][self.x + j - 3] - 1
                        if n == 23:
                            if self.gobl_killed >= 8:
                                n = 24
                            if self.gobl_killed >= 16:
                                n = 25
                        self.p[i][j].setPixmap(self.pixmap[n])

            if self.spisoc[self.y][self.x] == 34:
                self.y, self.x = random.choice(self.spisoc_34)
                for i in range(7):
                    for j in range(7):
                        n = self.spisoc[self.y + i - 3][self.x + j - 3] - 1
                        if n == 23:
                            if self.gobl_killed >= 8:
                                n = 24
                            if self.gobl_killed >= 16:
                                n = 25
                        self.p[i][j].setPixmap(self.pixmap[n])

            for i in range(10):
                xfg, yfg, nfg = self.fb[i].getcoord()
                if xfg >= 0 and yfg >= 0:
                    if self.spisoc[yfg][xfg] == 20:
                        self.spisoc[yfg][xfg] = 23
                        self.fb[i].setcoord(0, 0, 4)
                        self.p[yfg - self.y + 3][xfg - self.x + 3].setPixmap(self.pixmap[21])

            self.pw.setPixmap(self.pq)
            # Выводим человека
            self.pw.move(288, 288)

            # Выводим гоблина
            for i in range(len(self.gobls)):
                xg, yg, ng, xp = self.gobls[i].getcoord()
                if ng == 4:
                    self.gobl_killed += 1

                if xg >= self.x - 3 and xg <= self.x + 3 and yg >= self.y - 3 and yg <= self.y + 3:
                    self.gobls_pw[i].setPixmap(self.go[ng])
                    self.gobls_pw[i].move((xg - self.x + 3) * 96, (yg - self.y + 3) * 96)
                else:
                    self.gobls_pw[i].setPixmap(self.go[ng])
                    self.gobls_pw[i].move(-100, -100)
                self.gobls_pw[i].setPixmap(self.gobls[i].draw_xp(self.go[ng]))
            # рисуем фаербол
            for i in range(10):
                xg, yg, ng = self.fb[i].getcoord()
                if ng < 4:
                    self.fb_pw[i].setPixmap(self.fb_pix[ng])
                    self.fb_pw[i].move((xg - self.x + 3) * 96, (yg - self.y + 3) * 96)
                else:
                    self.fb_pw[i].setPixmap(self.fb_pix[ng])
                    self.fb_pw[i].move(-100, -100)

    def timerEvent(self, e):
        if self.st_time == 0:
            self.pw.setPixmap(self.pq)
            self.st_time = 1
        elif self.st_time == 1:
            self.pw.setPixmap(self.fb_pix[-1])
            self.st_time = 2
        elif self.st_time == 2:
            self.pw.setPixmap(self.pq)
            self.timer.stop()
        elif self.st_time == 3:
            self.p[3][3].setPixmap(self.pixmap[29])
            self.st_time = 4
        elif self.st_time == 3:
            self.p[3][3].setPixmap(self.pixmap[28])
            self.st_time = 4
        elif self.st_time == 4:
            self.p[3][3].setPixmap(self.pixmap[28])
            self.st_time = 5
        elif self.st_time == 5:
            self.p[3][3].setPixmap(self.pixmap[29])
            self.st_time = 6
        elif self.st_time == 6:
            self.p[3][3].setPixmap(self.pixmap[27])
            self.timer.stop()


class goblin():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.n = 0
        self.xp_normal = 200
        self.xp_max = 200
        self.skip = 0
        self.damage = 0

    def getcoord(self):
        return self.x, self.y, self.n, self.xp_normal

    def setcoord(self, spisoc, x, y, n, xp_n):
        if xp_n <= 0 and n < 4:
            xp_n = 0
            n = 4
        if spisoc[y][x] == 2:
            spisoc[self.y][self.x] -= 32
            self.x = x
            self.y = y
            spisoc[self.y][self.x] += 32
        self.n = n
        self.xp_normal = xp_n
        self.skip = 1

    def step(self, spisoc, xi, yi):
        self.damage = 0
        tx = self.x
        ty = self.y
        if self.skip:
            self.skip = 0
            return
        if self.n == 4:
            spisoc[self.y][self.x] -= 32
            self.n = 5
            return
        if self.n == 5:
            self.n = 6
            return
        if self.n == 6:
            return
        sn = [(self.y, self.x-1), (self.y - 1, self.x), (self.y, self.x + 1), (self.y+1, self.x)]
        sn_ = [1, 3, 0, 2]

        if self.g == 0:
            random.shuffle(sn_)
            for i in sn_:
                y, x = sn[i]
                if spisoc[y][x] == 2:
                    self.g = random.randint(1, 5)
                    self.n = i
                    if xi == self.x and yi >= self.y - 3 and yi <= self.y + 3 or yi == self.y and xi >= self.x - 3 and xi <= self.x + 3:
                        if xi == self.x and yi >= self.y and spisoc[yi][xi] == 2:
                            self.n = 3
                        if xi == self.x and yi <= self.y and spisoc[yi][xi] == 2:
                            self.n = 1
                        if yi == self.y and xi >= self.x and spisoc[yi][xi] == 2:
                            self.n = 2
                        if yi == self.y and xi <= self.x and spisoc[yi][xi] == 2:
                            self.n = 0
                        self.g = 10
                    break
        else:
            nst = self.n
            if xi == self.x and yi >= self.y - 3 and yi <= self.y + 3 or yi == self.y and xi >= self.x - 3 and xi <= self.x + 3:
                if xi == self.x and yi >= self.y and spisoc[yi][xi] == 2:
                    self.n = 3
                if xi == self.x and yi <= self.y and spisoc[yi][xi] == 2:
                    self.n = 1
                if yi == self.y and xi >= self.x and spisoc[yi][xi] == 2:
                    self.n = 2
                if yi == self.y and xi <= self.x and spisoc[yi][xi] == 2:
                    self.n = 0
                self.g = 10
            if nst == self.n:
                self.g -= 1
                y, x = sn[self.n]

                if spisoc[y][x] == 2:
                    spisoc[self.y][self.x] -= 32
                    self.x = x
                    self.y = y
                    spisoc[self.y][self.x] += 32
                else:
                    self.g = 0
                if self.x == xi and self.y == yi:
                    self.damage = 25
                    spisoc[self.y][self.x] -= 32
                    self.x = tx
                    self.y = ty
                    spisoc[self.y][self.x] += 32
        return self.x, self.y, self.n

    def getdamage(self):
        return self.damage

    def draw_xp(self, pix):
        self.p = pix.copy()
        if self.xp_normal != 0:
            self.pp = QPainter(self.p)
            self.pp.setPen(QColor(255, 0, 0))
            self.pp.drawRect(23, 0, 40, 3)
            self.pp.fillRect(23, 0, int(40 * (self.xp_normal / self.xp_max)), 3, QColor(255, 0, 0))
            self.pp.end()
        return self.p

    def kick(self, spisoc, n, xp):
        sn = [(self.y, self.x - 1), (self.y - 1, self.x), (self.y, self.x + 1), (self.y + 1, self.x)]
        y1, x1 = sn[n]
        self.setcoord(spisoc, x1, y1, self.n, self.xp_normal - xp)


class fireboll():

    def __init__(self):
        self.x = -100
        self.y = -100
        self.n = 4

    def setcoord(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

    def getcoord(self):
        return self.x, self.y, self.n

    def step(self, spisoc):
        if self.n > 3:
            return
        sn = [(self.y, self.x - 1), (self.y - 1, self.x), (self.y, self.x + 1), (self.y + 1, self.x)]
        h, j = sn[self.n]
        if h <= 0 or h >= len(spisoc):
            self.n = 4
            return
        if j <= 0 or j >= len(spisoc[0]):
            self.n = 4
            return
        if spisoc[h][j] == 0:
            self.n = 4
        else:
            self.y, self.x = sn[self.n]
            return



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
