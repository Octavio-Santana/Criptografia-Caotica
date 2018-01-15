# -*- coding: utf-8 -*-
import numpy as np
from scipy.integrate import odeint

class Codificador:
    def __init__(self, x0, y0, z0, msg):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.msg = msg

        # Condiçao inicial #
        inic = [self.x0, self.y0, self.z0]

        # Parametros #
        s = 10.0
        r = 28.0
        b = 8.0/3.0

        def lorentz_function(u, time):
            # u[0] = x, u[1] = y e u[2] = z #
            dx = s*( u[1] - u[0] )
            dy = u[0]*( r - u[2] ) - u[1]
            dz = u[0]*u[1] - b*u[2]
            return [dx, dy, dz]

        t = np.linspace(0,500,10000)
        tf = 0
        dt = 1
        k = 2.0/30

        while (k*len(t)) < len(self.msg):
            tf += 500
            dt *= 10
            t = np.linspace(0, 500+tf, 10000*dt)

        n = np.int(k*len(t))
        res = odeint(lorentz_function, inic, t)
        res_max = max(res[:,2])

        if ( res_max + 127 ) >= 255:
            res[:,2] = res[:,2]/255

        self.keys = [np.int(res[:,2][n+i*10]) for i in range(len(self.msg))]

class Encripta(Codificador):

    @property
    def encripta(self):
        self.s_enc = ''
        for i, m in enumerate(self.msg):
            self.s_enc += chr( abs(ord(m) + self.keys[i]) )
        return self.s_enc

class Decripta(Codificador):

    @property
    def decripta(self):
        self.s_dec = ''
        for i, m in enumerate(self.msg):
            self.s_dec += chr( abs(ord(m) - self.keys[i]) )
        return self.s_dec