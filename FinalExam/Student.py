#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.score = score
        self.name = name
    def isPassExam(self):
        return self.score >= 60
#def passfinalexam(name:)