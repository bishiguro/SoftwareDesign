# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo

Bonnie Ishiguro
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image   
from math import *

def build_random_function(min_depth, max_depth):
    # your doc string goes here

    xy = [["x"],["y"]] 
    if max_depth <= 1:
        return xy[randint(0,1)]  
    
    # create a list of building block functions   
    a = build_random_function(min_depth-1,max_depth-1)
    b = build_random_function(min_depth-1,max_depth-1)
    prod = ["prod",a,b]
    cos_pi = ["cos_pi",a]
    sin_pi = ["sin_pi",a]
    square = ["square",a]
    cube = ["cube",a]
    bb_functions=[prod,cos_pi,sin_pi,square,cube]
        
    if min_depth >= 1:
        return bb_functions[randint(0,len(bb_functions)-1)]
    
    # list of all functions : x, y, building block functions
    all_functions = xy + bb_functions
    return all_functions[randint(0,len(all_functions)-1)]    

def evaluate_random_function(f, x, y):
    # your doc string goes here       

    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    elif f[0] == "prod":
        return evaluate_random_function(f[1],x,y) * evaluate_random_function(f[2],x,y)
    elif f[0] == "cos_pi":
        return cos(pi * evaluate_random_function(f[1],x,y))
    elif f[0] == "sin_pi":
        return sin(pi * evaluate_random_function(f[1],x,y))
    elif f[0] == "square":
        return evaluate_random_function(f[1],x,y) ** 2
    elif f[0] == "cube":
        return evaluate_random_function(f[1],x,y) ** 3
        
def generate_image():
    im = Image.new("RGB",(350,350))
    
    red_func = build_random_function(9,14)
    blue_func = build_random_function(7,12)
    green_func = build_random_function(10,16)  
    
    for i in range(0,349):
        for j in range(0,349):
            x = remap_interval(i,0.,349,-1,1)     
            y = remap_interval(j,0.,349,-1,1)

            red = evaluate_random_function(red_func,x,y)
            blue = evaluate_random_function(blue_func, x,y)
            green = evaluate_random_function(green_func, x,y)

            red = int(remap_interval(red,-1,1,0,255))
            blue = int(remap_interval(blue,-1,1,0,255))
            green = int(remap_interval(green,-1,1,0,255))
            im.putpixel((i,j),(int(red),int(blue),int(green)))
    im.save("prettypic.bmp")
    im.show()

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """    
    return output_interval_end - (input_interval_end - val)/(input_interval_end - input_interval_start) * (output_interval_end - output_interval_start)