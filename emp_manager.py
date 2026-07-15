# starting sqlite3 new project
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# C:\Users\midom\OneDrive\Documents
# "C:\Users\midom\OneDrive\Documents\em_data.xlsx"

# employee App for any company
window = Tk()
window.title("EmP_Manager")
window.geometry("400x400")

e_data = sqlite3.connect("emp_data.db")
CuR = e_data.cursor()
CuR.execute("CREATE TABLE if not exists employee (name TEXT, ph_no INTEGER, secret_no INTEGER, career TEXT)")
e_data.commit()
e_data.close()

pass_l = Label(window, text="password                    ", font="consolas 13 bold")
pass_l.place(relx=0.4, rely=0.4, anchor="center")

password_e = Entry(window, width=25, font="Calibre 15 italic")
password_e.place(relx= 0.5, rely=0.4, anchor="center")

def open(event):
    password = password_e.get().lower()
    if password == "emp321":
        pass_l.destroy()
        password_e.destroy()
        # list of employees
        list_of_emp_data = Listbox(window, height=20, width=40, font="consolas 14 bold")
        list_of_emp_data.place(relx=0.002, rely=0.1)
        list_of_emp_data.insert(1, "Name : phone_no : career", "\n")


        # reading last Added data from the last open in the app
        def Show():
            reading = sqlite3.connect("emp_data.db")
            f_cur = reading.cursor()
            fetching = f_cur.execute("select * from employee")
            occurred_data = fetching.fetchall()
            for data in occurred_data:
                new_data = list(data)
                list_of_emp_data.insert(END, (new_data[0] ,new_data[1] ,new_data[3]))
            reading.commit()
            reading.close()

        # more information for each employee
        def Show_info(event):
            selected = list_of_emp_data.curselection()
            if selected:
                ind = selected[0]
                emp_select = list(list_of_emp_data.get(ind))
                det_Win = Toplevel(window)
                det_Win.geometry("300x300")
                det_Win.title("Details...")
                Label(det_Win, text=f"Name: {emp_select[0]}\n\nphone number: {emp_select[1]}\n\nCareer: {emp_select[2]}", font="Calibre 13 bold").pack(pady=15)

        def up_delete(event):
            Winn = Toplevel()
            Winn.title("Choose")
            Winn.geometry("350x140")
            Winn.resizable(False, False)

            # delete function
            def Kick():
                WinInWinn = Toplevel(window)
                WinInWinn.title("Deleting...")
                WinInWinn.geometry("500x230")
                WinInWinn.resizable(False, False)

                # Asking for secret Number (Label, Entry)
                SeCode_Label = Label(WinInWinn, text="Employee Secret_no. ", font="Calibre 14 bold")
                SeCode_Label.place(relx=0.02, rely=0.2)

                # Entry
                Secret_No = Entry(WinInWinn, width=25, font="consolas 14 italic")
                Secret_No.place(relx=0.44, rely=0.2)

                # remove button function
                def Kill():
                    try:
                        Secret = int(Secret_No.get())
                    except ValueError:
                        messagebox.showerror("Invalid input")
                        return # stop deleting
                    # connect to database
                    # deleting from database
                    del_conn = sqlite3.connect("emp_data.db")
                    del_cUr = del_conn.cursor()
                    del_cUr.execute(f"delete from employee where secret_no = {Secret}")
                    del_conn.commit()
                    del_conn.close()
                    # deleting from the listbox
                    selected2 = list_of_emp_data.curselection()
                    list_of_emp_data.delete(selected2)
                    messagebox.showinfo("Success", "The process is done successfully!!")
                    Retry()

                # remove and clear buttons
                # remove button
                remove_button = ttk.Button(WinInWinn, text="remove", command=Kill)
                remove_button.place(relx=0.1, rely=0.4)

                # clear button function
                def Retry():
                    Secret_No.delete(0, "end")
                    Secret_No.focus_set()

                # clear button
                clear_button = ttk.Button(WinInWinn, text="clear", command=Retry)
                clear_button.place(relx=0.3, rely=0.4)

                # update function
            def edit():
                sec_win = Toplevel(window)
                sec_win.title("Editing...")
                sec_win.geometry("400x450")

                # first taking the old sec_number
                # before editing
                old_no_label = Label(sec_win, text="Old Secret_No.   ", font="Calibre 14 bold")
                old_no_label.place(relx=0.1, rely=0.1)
                
                # entry for old No
                old_No = Entry(sec_win, width=20, font="consolas 13 bold")
                old_No.place(relx=0.5, rely=0.1)

                # main edit function
                def main():
                    # checking the secret_no
                    try:
                        wanted = int(old_No.get())
                    except ValueError:
                        messagebox.showerror("errrr", "Invalid input")
                    

                    # forming the screen first
                    old_no_label.destroy()
                    old_No.destroy()

                    # name label and field
                    N_Name_l = Label(sec_win, text="Name ", font="Calibre 12 bold")
                    N_Name_l.place(relx=0.1, rely=0.1)

                    #field
                    N_Name = Entry(sec_win, width=19, font="Calibre 11 bold")
                    N_Name.place(relx=0.3, rely=0.1)

                    # ph_no label and field
                    N_ph_no_l = Label(sec_win, text="Phone number ", font="Calibre 12 bold")
                    N_ph_no_l.place(relx=0.1, rely=0.2)

                    #field
                    N_ph_no = Entry(sec_win, width=19, font="Calibre 11 bold")
                    N_ph_no.place(relx=0.4, rely=0.2)

                    N_sec_no_l = Label(sec_win, text="Secret_No.  ", font="Calibre 12 bold")
                    N_sec_no_l.place(relx=0.1, rely=0.3)

                    #field
                    N_sec_no = Entry(sec_win, width=19, font="Calibre 11 bold")
                    N_sec_no.place(relx=0.4, rely=0.3)

                    N_career_l = Label(sec_win, text="Career ", font="Calibre 12 bold")
                    N_career_l.place(relx=0.1, rely=0.4)

                    #field
                    N_career = Entry(sec_win, width=19, font="Calibre 11 bold")
                    N_career.place(relx=0.3, rely=0.4)

                    # function for saving edited data
                    # for second save button
                    def New_rec():
                        # collecting new data
                        Name = N_Name.get()
                        
                        try:
                            ph_no = int(N_ph_no.get())
                            secret_no = int(N_sec_no.get())
                        except ValueError:
                            messagebox.showerror("ERRRRRRR..", "Invalid input in Secret_no.")
                        career = N_career.get()
                        try:
                            #connecting to database
                            edi_connection = sqlite3.connect("emp_data.db")
                            # starting to edit in database
                            edit_cursor = edi_connection.cursor()
                            edit_cursor.execute(f"update employee set name = '{Name}', ph_no = {ph_no}, secret_no = {secret_no}, career = '{career}' where secret_no = {wanted}")
                            edi_connection.commit()
                            edi_connection.close()
                            # saving new data in the list
                            selected2 = list_of_emp_data.curselection()
                            list_of_emp_data.delete(selected2)
                            list_of_emp_data.insert(END, (Name, ph_no, career))
                            messagebox.showinfo("Note...", "New data is saved successfully")
                            # checking if wanted variable is = to the secret_no as in the database
                        except sqlite3.OperationalError:
                            messagebox.showerror("ERRRRR", "Invalid input in one of the fields")
                            return # stop editing here
                        
                    # second save button
                    Save_new = ttk.Button(sec_win, text="Save New", command=New_rec)
                    Save_new.place(relx=0.1, rely=0.5)

                # second edit button
                edit_bu = ttk.Button(sec_win, text="Edit", command=main)
                edit_bu.place(relx=0.2, rely=0.2)



            # the two buttons (delete, update)
            # delete button
            delete_button = ttk.Button(Winn, text="delete", command=Kick)
            delete_button.place(relx=0.4, rely=0.5, anchor='center')

            # update button
            update_button = ttk.Button(Winn, text="Edit", command=edit)
            update_button.place(relx=0.7, rely=0.5, anchor='center')

        list_of_emp_data.bind('<Double-Button-1>', up_delete)
        list_of_emp_data.bind('<S>', Show_info)



        Show()

        # the search button
        search_L = Label(window, text="Search", font="consolas 13 bold")
        search_L.place(relx=0.3, rely=0.01)

        # search entry and it's button
        search_e = Entry(window, width=25, font="consolas 14 italic")
        search_e.place(relx=0.36, rely=0.01)

        # Search function
        def fetching(event):
            # getting data to search
            needed = search_e.get()
            # connect to data base
            connect = sqlite3.connect("emp_data.db")
            cursor = connect.cursor()
            cursor.execute(f"select name, ph_no, secret_no, career from employee where name = '{needed}'")
            
            result = cursor.fetchone()
            if result is None:
                messagebox.showinfo("nothing...", f"Did not find results for {needed}")
            else:
                # changing into list to hide the secret number
                Changing_data_to_list = list(result)
                showing = f"({Changing_data_to_list[0]}, {Changing_data_to_list[1]} , {Changing_data_to_list[3]})"

                # Label for showing columns
                Show_label1 = Label(window, text=" Name : phone_number : Career", font="Calibre 15 bold")
                Show_label1.place(relx=0.36, rely=0.15)

                # Label that shows fetched data
                Show_label = Label(window, text=f"{showing}", font="Calibre 15 bold")
                Show_label.place(relx=0.36, rely=0.2)

                # small function for clear button
                def Reset():
                    Show_label1.destroy()
                    Show_label.destroy()
                    search_e.delete(0, 'end')
                    search_e.focus_set()
                    Clear.destroy()
                
                # clear button (for clearing data after seeing it)
                Clear = ttk.Button(window, text="Reset", command=Reset)
                Clear.place(relx=0.36, rely=0.27)
            connect.close()

        window.bind('<Return>', fetching)



        # The Add button function
        def APPEND():
            # taking data and new screen
            winInwin = Toplevel(window)
            winInwin.title("Adding...")
            winInwin.geometry("500x320")
            winInwin.config(bg="light blue")
            winInwin.resizable(False, False)

            # showing the form of taking data
            name_label = Label(winInwin, text="name ", font="Calibre 12 bold", bg="light blue")
            name_label.place(relx=0.01, rely=0.1)

            name = Entry(winInwin, width=20)
            name.place(relx=0.13, rely=0.1)

            ph_no_label = Label(winInwin, text="Phone Number ", font="Calibre 11 bold", bg="light blue")
            ph_no_label.place(relx=0.01, rely=0.2)
            
            ph_no = Entry(winInwin, width=20)
            ph_no.place(relx=0.24, rely=0.2)

            Sec_c_label = Label(winInwin, text="Secret_code ", font="Calibre 11 bold", bg="light blue")
            Sec_c_label.place(relx=0.01, rely=0.3)
            
            Sec_code = Entry(winInwin, width=20)
            Sec_code.place(relx=0.24, rely=0.3)

            Career_label = Label(winInwin, text="Career ", font="Calibre 12 bold", bg="light blue")
            Career_label.place(relx=0.01, rely=0.4)
            
            Career = Entry(winInwin, width=20)
            Career.place(relx=0.13, rely=0.4)

            # save button function (action)
            def InSerT():
                # if name or ph_no or Sec_code or Career == False:
                #     messagebox.showerror("Missing data", "Please, fill all entries To save data!!")
                #     return # Stop everything after this

                # taking data
                em_name = name.get().title()
                try:
                    em_ph_no = int(ph_no.get())
                    em_secret_code = int(Sec_code.get())
                except ValueError:
                    messagebox.showerror("ERRRR", "Invalid input")
                    return # stop Adding here
                
                em_career = Career.get()
                # connection to database
                e_data = sqlite3.connect("emp_data.db")
                CuR = e_data.cursor()
                CuR.execute("CREATE TABLE if not exists employee (name TEXT, ph_no INTEGER, secret_no INTEGER, career TEXT)")
                
                # Adding data to database
                CuR.execute("insert into employee (name, ph_no, secret_no, career) values (?, ?, ?, ?)", (em_name, em_ph_no, em_secret_code, em_career))
                e_data.commit()
                # Adding this new data to the listbox
                list_of_emp_data.insert(END, (em_name ,em_ph_no ,em_career))
                e_data.close()
                messagebox.showinfo("Done", "The process is done successfully")
                erase()

            # Clear button function (action)
            def erase():
                name.delete(0, "end")
                ph_no.delete(0, "end")
                Sec_code.delete(0, "end")
                Career.delete(0, "end")
                name.focus_set()

            # buttons Save and clear
            Save = ttk.Button(winInwin, text="Save", command=InSerT)
            Save.place(relx=0.1, rely=0.53)
            
            Clear = ttk.Button(winInwin, text="Clear", command=erase)
            Clear.place(relx=0.26, rely=0.53)


        # the Add button
        Add = ttk.Button(window, text="Add +", command=APPEND)
        Add.place(relx=0.002, rely=0.01)

    else:
        messagebox.showerror("errrrrr", "Sorry, the password is wrong\nplease write the rigth password")


window.bind('<Return>', open)

window.mainloop()