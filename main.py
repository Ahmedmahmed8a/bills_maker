import kivy  
from datetime import datetime
from functools import partial
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.11.1')
class MyApp(App):
 
 
 def makebill(self,name,admin,arr,event):
 	self.bill.clear_widgets()
 	cname=str(name.text)
 	head=f"\tTo: %s\n\tFrom: %s\n\tDate: %s"%(cname,admin.text,datetime.now())
 	cmr=Label(text=head)
 	self.bill.add_widget(cmr)
 	
 	self.bill.sheet=GridLayout(cols=4)
 	
 	c1=Label(text='id',size_hint_x=2)
 	c2=Label(text='description', size_hint_x=6)
 	c3=Label(text='qty',size_hint_x=2)
 	c4=Label(text='amount',size_hint_x=3)
 	self.bill.sheet.add_widget(c1)
 	self.bill.sheet.add_widget(c2)
 	self.bill.sheet.add_widget(c3)
 	self.bill.sheet.add_widget(c4)
 	self.id=TextInput(readonly=True,size_hint_y=12)
 	self.des=TextInput(readonly=True)
 	self.qty=TextInput(readonly=True)
 	self.amt=TextInput(readonly=True)
 	self.bill.sheet.add_widget(self.id)
 	self.bill.sheet.add_widget(self.des)
 	self.bill.sheet.add_widget(self.qty)
 	self.bill.sheet.add_widget(self.amt)
 	amts=[]
 	y=0
 	for i in range(len(arr)):
 		self.id.text=self.id.text+"\n"+arr[i][0]
 		self.des.text=self.des.text+"\n"+arr[i][1]
 		self.qty.text=self.qty.text+"\n"+arr[i][2]
 		x=float(arr[i][2])*float(arr[i][3])
 		self.amt.text=self.amt.text+"\n"+str(x)
 		amts.append(x)
 	self.tids=TextInput(readonly=True)
 	self.tdes=TextInput(readonly=True,text="Total")
 	self.tqty=TextInput(readonly=True)
 	self.tamt=TextInput(readonly=True,text=str(sum(amts)))
 	self.bill.sheet.add_widget(self.tids)	
 	self.bill.sheet.add_widget(self.tdes)
 	self.bill.sheet.add_widget(self.tqty)
 	self.bill.sheet.add_widget(self.tamt)
 	self.bill.add_widget(self.bill.sheet)
 def clear(self,arr,event):
 	self.items.text=""
 	arr=[]
 	self.ary=[]
 def add(self,arr,event):
 	arr.append([
 	self.dc1.text
 	,self.dc2.text
 	,self.dc3.text
 	,self.dc4.text]
 	)
 	self.ary=arr
 	for i in range(len(self.ary)):
 		self.items.text=self.items.text+"\n"+str(self.ary[i])
 def build(self):
  self.ary=[]
  bill_pad=[100,100,100,100]
  self.bill = GridLayout(cols=1,padding=bill_pad,spacing=45)
  self.bill.add_widget(Label(text="Welcome :)",font_size="72",size_hint=(100,None)))
  self.items=TextInput(multiline=True,font_size="32" ,size_hint_y=None,height=300)
  self.bill.add_widget(self.items)
  grb=GridLayout(cols=4,size_hint_y=None)
  self.dc1=TextInput(hint_text="id",multiline=False,font_size="32" ,size_hint_y=None,height=100-42,input_filter="float")
  self.dc2=TextInput(hint_text="describtion",multiline=False,font_size="32" ,size_hint_y=None,height=100-42)
  self.dc3=TextInput(hint_text="qty",multiline=False,font_size="32" ,size_hint_y=None,height=100-42,input_filter="float")
  self.dc4=TextInput(hint_text="price",multiline=False,font_size="32" ,size_hint_y=None,height=100-42,input_filter="float")
  grb.add_widget(self.dc1)
  grb.add_widget(self.dc2)
  grb.add_widget(self.dc3)
  grb.add_widget(self.dc4)
  self.bill.add_widget(grb)
  grb1=GridLayout(cols=2,spacing=5,size_hint_y=None)
  self.add_btn=Button(text="Add")
  self.clr_btn=Button(text="Clear")
  grb1.add_widget(self.add_btn)
  grb1.add_widget(self.clr_btn)
  self.add_btn.bind(on_press=partial(self.add,self.ary))
  self.clr_btn.bind(on_press=partial(self.clear,self.ary))
  self.bill.add_widget(grb1)
  admin=TextInput(hint_text="Admin",text="Ahmed",multiline=False,font_size="32" ,size_hint_y=None,height=100-42)
  self.bill.add_widget(admin)
  customer=TextInput(hint_text="Customer name",multiline=False,font_size="32" ,size_hint_y=None,height=100-42)
  
  self.bill.add_widget(customer)
  self.button=Button(text="New Bill",size_hint=(100,None))
  
  self.bill.add_widget(self.button)
  self.button.bind(on_press=partial(self.makebill,customer,admin,self.ary))
  
  return self.bill
  
if __name__ == '__main__':
    MyApp().run()