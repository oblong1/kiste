# -*- coding: utf-8 -*-

"""A Class who represents a chessplayer with ELO and DWZ."""

class Player():
    
    def __init__(self, name, vorname, elo, dwz):
        self.name = name
        self.vorname = vorname
        self.elo = elo
        self.dwz = dwz

    def get_fullname(self):
        print(self.name.title() + ", " + self.vorname.title())
    