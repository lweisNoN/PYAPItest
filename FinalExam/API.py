#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Student import Student

def callApi(json):
    student = Student(json['name'], json['score'])
    isPass = student.isPassExam()
    return (student.name, isPass)
