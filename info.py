from tkinter import *
import random
import tkinter.messagebox
import json
my_email = "lordarglax@gmail.com"
my_pass = "fluerdelamort1"


QUESTIONS_FONT = ("Consolas" , 11 , "normal")
BG = "beige"
class Info:
	def random( self ):
		choices = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' ,
		           'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' ,
		           'Y' , 'Z' , '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
		generated = []
		for char in range(0 , 5):
			generated.append(random.choice(choices))
		code = generated
		code = ''.join(code)
		self.applications_code = code
	def done( self ):
		self.random()
		confirm = tkinter.messagebox.askyesnocancel(title="Confirmation" , message="Are you sure that you have inputted all fields correctly?")
		person_data = {
			self.applications_code: {
				"Name": self.entry_name.get() ,
				"Sex": self.sex_choice.get() ,
				"Age": self.contact.get() ,
				"Contact": self.contact.get() ,
				"ID Number": self.ID.get() ,
				"Birthday": (self.m.get() , self.d.get() , self.y.get()) ,
				"Address": self.address.get() ,
				"Violations": (self.violation.get() , self.violation2.get() , self.violation3.get()) ,
				"Date of Incident": (self.mv.get() , self.dv.get() , self.yv.get()) ,
				"Place of Incident": self.incident.get() ,
				"Arresting Officer": self.officer.get() ,
				"Email of Officer":self.email.get(),
				"Details": self.additional.get()
			}
		}
		if confirm:
			print(self.applications_code)
			try:
				with open("applications.json" , mode="r") as user_info:
					get_data = json.load(user_info)
			except FileNotFoundError:
				with open("applications.json" , mode="w") as user_info:
					json.dump(person_data , user_info , indent=4)
			else:
				get_data.update(person_data)
				with open("applications.json" , mode="w") as user_info:
					json.dump(get_data , user_info , indent=4)
			finally:
				self.print_data()

	def print_data( self ):
		print(self.applications_code)
		try:
			with open("applications.json" , mode="r") as print_existing:
				search_application_code = json.load(print_existing)
		except FileNotFoundError:
			tkinter.messagebox.showinfo("The List of Applications file might have been deleted.")
		else:
			if self.applications_code in search_application_code:
				name = search_application_code[self.applications_code]["Name"]
				sex = search_application_code[self.applications_code]["Sex"]
				age = search_application_code[self.applications_code]["Age"]
				contact = search_application_code[self.applications_code]["Contact"]
				id_num = search_application_code[self.applications_code]["ID Number"]
				birthday_m = search_application_code[self.applications_code]["Birthday"][0]
				birthday_d = search_application_code[self.applications_code]["Birthday"][1]
				birthday_y = search_application_code[self.applications_code]["Birthday"][2]
				address = search_application_code[self.applications_code]["Address"]
				violations_1 = search_application_code[self.applications_code]["Violations"][0]
				violations_2 = search_application_code[self.applications_code]["Violations"][1]
				violations_3 = search_application_code[self.applications_code]["Violations"][2]
				i_1 = search_application_code[self.applications_code]["Date of Incident"][0]
				i_2 = search_application_code[self.applications_code]["Date of Incident"][1]
				i_3 = search_application_code[self.applications_code]["Date of Incident"][2]
				place_of_incident = search_application_code[self.applications_code]["Place of Incident"]
				arresting_officer = search_application_code[self.applications_code]["Arresting Officer"]
				email = search_application_code[self.applications_code]["Email of Officer"]
				details = search_application_code[self.applications_code]["Details"]
				to_send  = name+".doc"
				with open(to_send,mode = "w") as infos:
					infos.write(f"Name: {name}\n")
					infos.write(f"Sex: {sex}\n")
					infos.write(f"Age: {age}\n")
					infos.write(f"Contact: {contact}\n")
					infos.write(f"Vehicle ID Number: {id_num}\n")
					infos.write(f"Birthday: {birthday_m} / {birthday_d} / {birthday_y}\n")
					infos.write(f"Address: {address}\n")
					infos.write(f"Violations: {violations_1}\n\t\t{violations_2}\n\t\t{violations_3}\n")
					infos.write(f"Date of Violation: {i_1} / {i_2} / {i_3}\n")
					infos.write(f"Place of Incident: {place_of_incident}\n")
					infos.write(f"Arresting Officer: {arresting_officer}\n")
					infos.write(f"Details of the Incident: {details}\n")
					infos.write(f"\n\nThis document is emailed at {email} for verification.\n")
					p = MIMEBase('application' , 'octet-stream')
					p.set_payload(to_send.read())
					encoders.encode_base64(to_send)
					p.add_header('Content-Disposition' , "attachment; filename= %s" % to_send)
					msg.attach(p)
					with smtplib.SMTP("smtp.gmail.com" , port=587) as connection:
						connection.starttls()
						connection.login(user=my_email , password=my_pass)
						connection.sendmail(from_addr=my_email , to_addrs=email, msg=f"Subject:{name} Violation Summary\n\n{send}")
			else:
				tkinter.messagebox.showinfo(title = "Non-existing Account",message = f"There is no records of Application Record Code:{self.applications_code}")
	def __init__( self ):
		self.window = Tk()
		self.window.title("Violation Recorder for Vehicle Impoundment")
		self.window.config(padx=30 , pady=10 , bg=BG)
		self.window.resizable(0 , 1)
		self.canvas = Canvas()
		self.title = Label(text="Complaint Proforma-Physical Contact Apprehension Records" , font=("Consolas" , 11 , "bold") , bg=BG).grid(column=0 , row=0 , columnspan=2)
		# LABELS
		self.label_name = Label(text="Name:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=1 , sticky="w" , pady=3)
		self.label_sex = Label(text="Sex:" , font=QUESTIONS_FONT , bg=BG).grid(column=1 , row=2 , pady=3)
		self.label_contact = Label(text="Contact:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=3 , sticky="w" , pady=3)
		self.label_age = Label(text="Age:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=2 , sticky="w" , pady=3)
		self.label_ID = Label(text="ID Number:" , font=QUESTIONS_FONT , bg=BG).grid(column=1 , row=3 , pady=3)
		self.label_address = Label(text="Address:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=6 , sticky="w" , pady=3)
		self.label_incident = Label(text="Violation/s:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=7 , sticky="w" , pady=3)
		self.label_incident_place = Label(text="Place of Incident:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=11 , sticky="w" , pady=3)
		self.label_officer = Label(text="Arresting Officer:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=12 , pady=3 , sticky="w")
		self.label_additional = Label(text="Details:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=13 , sticky="w" , pady=3)
		self.label_email = Label(text="Email of Officer:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=14 , sticky="w" , pady=3)
		# ENTRIES
		self.entry_name = Entry(width=50)
		self.entry_name.grid(column=1 , row=1 , pady=3)
		self.sex_choice = Entry(width=20)
		self.sex_choice.grid(column=1 , row=2 , sticky="e" , pady=3)
		self.entry_age = Entry(width=20)
		self.entry_age.grid(column=1 , row=2 , sticky="w" , pady=3)
		self.contact = Entry(width=16)
		self.contact.grid(column=1 , row=3 , sticky="w" , pady=3)
		self.ID = Entry(width=18)
		self.ID.grid(column=1 , row=3 , sticky="e" , pady=3)
		self.address = Entry(width=50)
		self.address.grid(column=1 , row=6 , columnspan=3 , pady=3)
		self.violation = Entry(width=50)
		self.violation.grid(column=1 , row=7 , columnspan=3 , pady=3)
		self.violation2 = Entry(width=50)
		self.violation2.grid(column=1 , row=8 , columnspan=3 , pady=3)
		self.violation3 = Entry(width=50)
		self.violation3.grid(column=1 , row=9 , columnspan=3 , pady=3)
		self.incident = Entry(width=50)
		self.incident.grid(column=1 , row=11 , columnspan=3 , pady=3)
		self.officer = Entry(width=50)
		self.officer.grid(column=1 , row=12 , pady=3)
		self.additional = Entry(width=50)
		self.additional.grid(column=1 , row=13 , pady=3)
		self.email = Entry(width=50)
		self.email.grid(column=1 , row=14 , pady=3)
		# BIRTHDAYS
		self.l_birthday = Label(text="Birthday:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=4 , sticky="w" , pady=3)
		b_month = Entry(width=15)
		b_month.insert(0 , "Month")
		self.m = b_month
		self.m.grid(column=1 , row=4 , sticky="w")
		b_day = Entry(width=15)
		b_day.insert(0 , "Day")
		self.d = b_day
		self.d.grid(column=1 , row=4)
		b_year = Entry(width=15)
		b_year.insert(0 , "Year")
		self.y = b_year
		self.y.grid(column=1 , row=4 , sticky="e")
		# VIOLATIONS
		self.l_violation = Label(text="Date of Incident:" , font=QUESTIONS_FONT , bg=BG).grid(column=0 , row=10 , sticky="w" , pady=3)
		v_month = Entry(width=15)
		v_month.insert(0 , "Month")
		self.mv = v_month
		self.mv.grid(column=1 , row=10 , pady=3)
		v_day = Entry(width=15)
		v_day.insert(0 , "Day")
		self.dv = v_day
		self.dv.grid(column=1 , row=10 , sticky="w" , pady=3)
		v_year = Entry(width=15)
		v_year.insert(0 , "Year")
		self.yv = v_year
		self.yv.grid(column=1 , row=10 , sticky="e" , pady=3)
		# BUTTON
		self.button_okay = Button(text="Done" , width=15 , command=self.done)
		self.button_okay.grid(column=1 , row=16 , sticky="e" , pady=5)
		# WINDOWS.LOOP
		self.window.mainloop()
	def remove( self ):
		print(self.applications_code)
		self.entry_name.delete(0 , END)
		self.entry_age.delete(0 , END)
		self.sex_choice.delete(0 , END)
		self.contact.delete(0 , END)
		self.contact.delete(0 , END)
		self.ID.delete(0 , END)
		self.m.delete(0 , END)
		self.d.delete(0 , END)
		self.y.delete(0 , END)
		self.address.delete(0 , END)
		self.violation.delete(0 , END)
		self.violation2.delete(0 , END)
		self.violation3.delete(0 , END)
		self.mv.delete(0 , END)
		self.dv.delete(0 , END)
		self.yv.delete(0 , END)
		self.incident.delete(0 , END)
		self.officer.delete(0 , END)
		self.additional.delete(0 , END)
