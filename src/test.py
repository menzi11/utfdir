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
    tmp = os.path.splitext(filename)[1];
    if tmp != b'.h' and tmp != b'.cpp' and tmp != b'.txt' and tmp != b'.TXT' :
    #print( code['encoding'] )
        print('1')
        print( tmp )
        return
    context = handle.read()
    code = chardet.detect(context)
    if code['encoding'] == None :
        print('3')
        return
    if code['encoding'] != 'UTF-8-SIG' and code['encoding'] != 'ascii' :
        print('2')
        print( code['encoding'] )
        print('检测到' + code['encoding'] + '编码,在文件:'+ filename.decode('gbk') + "中,开始转码!" )
        output_context = context.decode( code['encoding'] ,'ignore')
        #print( type(output_context) )
        open(filename, 'wb').write( output_context.encode('utf-8') )

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
            #print( name.decode('gbk') )
            GBK_to_UTF8_withBOM( os.path.join(root, name) )
            #tab_to_4_space( os.path.join(root, name) )
            #printGBK( name ) #Chinese(name)
            print( "---------------" )

walk_dir(u"C:\wkspaces\Heavier7Strings\src".encode('gbk'))