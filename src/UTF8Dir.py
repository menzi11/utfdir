#!/usr/bin/python
# -*- coding: utf-8 -*-

##2、os.walk方法
#os模块提供的walk方法很强大，能够把给定的目录下的所有目录和文件遍历出来。
#方法：os.walk(path),遍历path，返回一个对象，他的每个部分都是一个三元组,('目录x'，[目录x下的目录list]，目录x下面的文件)
import os
import chardet
import types

def Chinese(text):
    return unicode(text, 'utf8').encode('gbk')

def printGBK(text):
    result = chardet.detect(text)
    print( result )
    if result['confidence'] < 0.7 :
        result['encoding'] = 'GBK'
    print( unicode( text , result['encoding'] ).encode('utf8') )

def GBK_to_UTF8_withBOM(filename) :
    handle = open(filename , "rb")
    context = handle.read()
    code = chardet.detect(context)
    tmp = os.path.splitext(filename)[1];
    if tmp != '.h' and tmp != '.cpp' and tmp != '.txt' :
        return
    if code['encoding'] == None :
        return
    if code['encoding'] != 'UTF-8-SIG' and code['encoding'] != 'ascii' :
        tmp2 = filename.decode('gbk').encode('utf8')
        print( tmp2 )
        print( code['encoding'] )
        printGBK('检测到' + code['encoding'] + '编码,在文件:'+ tmp2 + "中,开始转码!" )
        output_context = context.decode( code['encoding'] ).encode('UTF-8-SIG')
        open(filename, 'w').write(output_context)

def tab_to_4_space(filename) :
    tmp = os.path.splitext(filename)[1];
    if tmp != '.h' and tmp != '.cpp' and tmp != '.txt' :
        return
    handle = open(filename , "rb")
    context = handle.read()
    code = chardet.detect(context)
    print( filename )
    if code['encoding'] != None and code['encoding'] != 'UTF-8-SIG' and code['encoding'] != 'ascii' :
        print( code['encoding'] )
        raise Exception("Invalid level!")
    if code['encoding'] != None :
        context = context.decode( code['encoding'] )
        text = context.replace('\t','    ')
        open(filename, 'w').write(text)

def walk_dir(dir):
    for root, dirs, files in os.walk( dir ):
        #print(root)
        #print "---------------"
        #print(dirs)
        #print Chinese(files)
        for name in files:
            GBK_to_UTF8_withBOM( os.path.join(root, name) )
            tab_to_4_space( os.path.join(root, name) )
            #printGBK( name ) #Chinese(name)
            print( "---------------" )

walk_dir(u"C:\wkspaces\Heavier7Strings\externals".encode('gbk'))