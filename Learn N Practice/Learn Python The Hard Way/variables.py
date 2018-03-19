# -*- coding: utf-8 -*-
name = "Anilkumar Adhikari";
age = 28;
height = 5.11;
weight = 158.123456
eyes = "Blue";
teeth = "White";
hair = "Black";

print "I'm %s" %name;
print "Am %.2f foot tall and %.2d pounds heavy." %(height, weight);
print "weight %d, eyes %s" %(weight, eyes);
print "weight %.2f, eyes %s" %(weight+age, eyes);
# Below line prints 'First argument: 47, second one: 11'
print "First argument: {0}, second one: {1}".format(47,11)
print " I'm {0:s}, and my age is {1:d}".format(age, name);