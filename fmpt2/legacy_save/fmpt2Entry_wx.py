'''
Created on 2018/2/23

@author: hitpony
'''

#!/usr/bin/python3.6
#-*- coding: UTF-8 -*-

import random
import sys
import time
import json
import os
import re
import urllib
import http
import socket
import wx
import wx.xrc
import gettext
_ = gettext.gettext



class Fmpt2Window(wx.Frame):
    """We simply derive a new class of Frame."""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (600, 400))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        #self.control = wx.Dialog(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar()

        #璁剧疆鑿滃崟
        L1menuFunc = wx.Menu()
        L1menuHelp = wx.Menu()

        #L1menuFunc
        L2ItemFunc1 = L1menuFunc.Append(wx.ID_FILE1, u"鍔熻兘1", u"鍔熻兘1")
        L2ItemFunc2 = L1menuFunc.Append(wx.ID_FILE1, u"鍔熻兘2", u"鍔熻兘2")
        L2ItemFunc3 = L1menuFunc.Append(wx.ID_FILE1, u"鍔熻兘3", u"鍔熻兘3")
        L2ItemFunc4 = L1menuFunc.Append(wx.ID_FILE1, u"鍔熻兘4", u"鍔熻兘4")

        #L1menuHelp
        L2ItemOption = L1menuHelp.Append(wx.ID_SAVE, u"璁剧疆", u"绯荤粺鍙傛暟璁剧疆")
        L2ItemHelp = L1menuHelp.Append(wx.ID_HELP, u"甯姪", u"甯姪淇℃伅")
        L2ItemAbout = L1menuHelp.Append(wx.ID_ABOUT, u"鍏充簬", u"鍏充簬绋嬪簭鐨勪俊鎭�")
        L1menuHelp.AppendSeparator()
        L2ItemExit = L1menuHelp.Append(wx.ID_EXIT, u"閫�鍑�", u"缁堟搴旂敤绋嬪簭")

        #鍒涘缓鑿滃崟鏍�
        menuBar = wx.MenuBar()
        menuBar.Append(L1menuFunc, u"鍔熻兘")
        menuBar.Append(L1menuHelp, u"甯姪")
        self.SetMenuBar(menuBar)

        #浜嬩欢澶勭悊event handling
        self.Bind(wx.EVT_MENU, self.OnFunc1, L2ItemFunc1)
        self.Bind(wx.EVT_MENU, self.OnFunc2, L2ItemFunc2)
        self.Bind(wx.EVT_MENU, self.OnFunc3, L2ItemFunc3)
        self.Bind(wx.EVT_MENU, self.OnFunc4, L2ItemFunc4)
        self.Bind(wx.EVT_MENU, self.OnOption, L2ItemOption)
        self.Bind(wx.EVT_MENU, self.OnHelp, L2ItemHelp)
        self.Bind(wx.EVT_MENU, self.OnAbout, L2ItemAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, L2ItemExit) 
        
        #璁剧疆sizers
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.SHAPED)    

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)    
        self.sizer.Add(self.sizer2, 0, wx.GROW)    

        # 婵�娲籹izer
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)     
        
        
        #鐢诲浘
        self.Show(True)

    def OnFunc1(self, e):
        pass

    def OnFunc2(self, e):
        pass

    def OnFunc3(self, e):
        pass    

    def OnFunc4(self, e):
        pass    
        
    def OnOption(self, e):
        pass        
        
    def OnHelp(self, e):
        dlg = wx.MessageDialog(self, "瀵绘眰甯姪", "FMPT2");
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnAbout(self, e):
        # 鍒涘缓涓�涓甫"OK"鎸夐挳鐨勫璇濇銆倃x.OK鏄痺xWidgets鎻愪緵鐨勬爣鍑咺D
        dlg = wx.MessageDialog(self, "宸ュ巶鐢熶骇绠＄悊宸ュ叿 V2", \
            "FMPT2", wx.OK)    # 璇硶鏄�(self, 鍐呭, 鏍囬, ID)
        dlg.ShowModal()    # 鏄剧ず瀵硅瘽妗�
        dlg.Destroy()    # 褰撶粨鏉熶箣鍚庡叧闂璇濇
    
    def OnExit(self, e):
        self.Close(True)    # 鍏抽棴鏁翠釜frame    
        

class MyWindow(wx.Frame):  
   
    def __init__(self):  
        wx.Frame.__init__(self, parent=None,title="My Test Frame",pos = (100,100), size=(500,450))  
          
        #娣诲姞绗�1涓狿anel闈㈡澘  
        panel1 = wx.Panel(parent=self,pos = (0,80), size=(225, 250))  
        panel1.Bind(wx.EVT_MOTION,  self.OnPanel1Move)  
        #娣诲姞鍏朵粬鎺т欢  
        wx.StaticText(parent=panel1, label= " Cursor Pos:", pos=(10, 10),size=(100, 25))  
        self.posCtrl1 = wx.TextCtrl(parent=panel1, value = "0,0", pos=(100, 10),size=(100, 25))  
          
        #娣诲姞绗�2涓狿anel闈㈡澘  
        panel2 = wx.Panel(parent=self,pos = (275,80), size=(225, 250))  
        #娣诲姞鍏朵粬鎺т欢  
        wx.StaticText(parent=panel2,label= " The Second Panel", pos=(10, 50),size=(150, 25))  
        self.btn=wx.Button(parent=panel2,label= " My Button",pos=(10, 100),size=(150, 25))  
        self.btn.Bind(wx.EVT_BUTTON,  self.OnMyButtonClick)  
          
        #娣诲姞wxStatusBar宸ュ叿鏉�  
        self.sb=self.CreateStatusBar(number =3)  
        self.SetStatusText("One",0)  
        self.SetStatusText("Two",1)  
        self.SetStatusText("Three",2)  
  
        #娣诲姞wxToolBar  
        self.tb=self.CreateToolBar()  
        bitmap1 = wx.Bitmap.FromRGBA(32, 24, red=0, green=0, blue=0, alpha=100)  
        self.tb.AddSeparator()  
        self.tb.AddTool(1,'',bitmap1)  
        self.tb.AddSeparator()  
        bitmap2 = wx.Bitmap.FromRGBA(32, 24, red=0, green=0, blue=0, alpha=150)          
        self.tb.AddTool(2,'',bitmap2)          
        self.tb.Realize()  
          
        #娣诲姞wxMenuBar鑿滃崟,鎻愪緵浜嗗嚑绉嶅垱寤鸿彍鍗曠殑鏂瑰紡  
        menubar = wx.MenuBar()  
        #涓�绾т富鑿滃崟  
        file = wx.Menu()  
        file.Append(-1, '&New')  
        file.Append(-1, '&Open')  
        file.Append(-1, '&Save')  
        file.AppendSeparator()  
        #澶氱骇瀛愯彍鍗�  
        imp = wx.Menu()   
        imp.Append(-1, 'Import newsfeed list...')  
        imp.Append(-1, 'Import bookmarks...')  
        imp.Append(-1, 'Import mail...')  
  
        file.Append(-1, 'I&mport', imp)  
        file.AppendSeparator()  
        #鍐嶆坊鍔犱竴涓彍鍗�  
        quit = wx.MenuItem(file, wx.ID_CLOSE, '&Quit/tCtrl+W')  
        self.Bind(wx.EVT_MENU, self.OnQuit, id=wx.ID_CLOSE) #缁戝畾鏂规硶  
        file.Append(quit)  
  
        menubar.Append(file, '&File')  
        self.SetMenuBar(menubar)  
          
        self.Centre() #灞呬腑鏄剧ず  
        self.Show(True)#鎬绘槸涓�鍒涘缓灏辨樉绀篎rame妗嗘灦,  
  
  
          
        #瀹氫箟浜嬩欢鏂规硶  
    def OnPanel1Move(self, event): #鍦≒anel1涓婇潰绉诲姩鐨勬椂璋冪敤  
        pos = event.GetPosition()  
        self.posCtrl1.SetValue("%s, %s" % (pos.x, pos.y))  
          
    def OnMyButtonClick(self,event): #鍦ㄦ寜閽笂闈㈠崟鍑昏皟鐢�  
        self.btn.SetLabel("You Clicked!")  
          
    def OnQuit(self, event): #鐐瑰嚮閫�鍑鸿彍鍗曟椂璋冪敤  
        self.Close()  
        

class MyPanel2 ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1220,529 ), style = wx.TAB_TRAVERSAL )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gbSizer1.Add( self.m_staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        #self.m_animCtrl3 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE ) 
        #gbSizer1.Add( self.m_animCtrl3, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_bitmap4, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_textCtrl4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        gbSizer1.Add( self.m_staticText6, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( gbSizer1 )
        self.Layout()
    
    def __del__( self ):
        pass


    
class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 511,396 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"label" ), wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        sbSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        sbSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel1.SetSizer( sbSizer1 )
        self.m_panel1.Layout()
        sbSizer1.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl6 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 490,150 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_RICH2 )
        bSizer4.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

        self.m_panel7 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"label" ), wx.HORIZONTAL )

        self.m_checkBox2 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_checkBox2, 0, wx.ALL, 5 )

        self.m_checkBox3 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_checkBox3, 0, wx.ALL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        sbSizer2.Add( self.m_choice1, 0, wx.ALL, 5 )

        self.m_button6 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_button6, 0, wx.ALL, 5 )

        self.m_button7 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_button7, 0, wx.ALL, 5 )


        self.m_panel7.SetSizer( sbSizer2 )
        self.m_panel7.Layout()
        sbSizer2.Fit( self.m_panel7 )
        bSizer4.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl7 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.Point( 10,10 ), wx.Size( 350,30 ), 0 )
        bSizer2.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( bSizer2 )
        self.m_panel3.Layout()
        bSizer2.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 3, wx.ST_ELLIPSIZE_MIDDLE, wx.ID_ANY )
        self.m_statusBar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
        self.m_statusBar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

def main():
    fmpt2App = wx.App(False)
    frame = Fmpt2Window(None, '宸ュ巶鐢熶骇宸ュ叿-FMPT2')
    #frame = MyWindow()
    #frame = MyFrame1(None)
    fmpt2App.MainLoop()    
    
#绯荤粺鍏ュ彛
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    