from User import User
from Database import Database as db
from Task import Task
from Vehicle import Vehicle
from License import License
from Number import Number
from transfer import transfer
from details_email import details_email
from Admin import Admin
import string
from random import *
from _tracemalloc import stop
def accountMenu(current_user):
    choice = -1
    
    while choice != '3':
        print('\n')
        print('1. New Vehicle Registration')
        print('2. Driver License Registration')
        print('3. User Menu')
        
        choice = input('Enter your choice: ')
        if(choice == '1'):
            user_id = input('User id (Case-Sensitive): ')
            vehicle_no = input('Vehicle No.: ').upper()
            vehicle_type = input('Vehicle Type (2/4 Wheeler): ').upper()
            vehicle_name = input('Vehicle Name: ').upper()
            vehicle_model = input('Vehicle Model: ').upper()
            vehicle_color = input('Vehicle Color: ').upper()
            vehicle_owner = input('Vehicle Owner Name: ').upper()
            vehicle_year = int(input('Vehicle Purchase Year: '))
            new_vehicle = Vehicle(user_id, vehicle_no, vehicle_type, vehicle_name, vehicle_model, vehicle_color, vehicle_owner, vehicle_year)

            if((User.authenuser_id(user_id)) and (new_vehicle.save())):
                print("")
                print('Your New Vehicle Got Registred!')
            else:
                print("")
                print('Sorry Vehicle not Registred! Note: Check User ID')
        elif(choice == '2'):
            user_id = input('User id (Case-Sensitive): ')
            license_no = input('Enter your License no.: ').upper()
            driver_name = input('Enter Driver Name: ').upper()
            issue_year = int(input('Issued Year: '))
            expire_year = int(input('Expire Year (Valid Upto): '))
            issue_authority = input('Issue Authority: ').upper()
            vehicle_type = input('Vehicle Type (2/4 Wheeler): ').upper()
            new_license = License(user_id, license_no, driver_name, issue_year, expire_year, issue_authority, vehicle_type)

            if((User.authenuser_id(user_id)) and (new_license.save())):
                print("")
                print('Your License Got Registred!')
            else:
                print("")
                print('Sorry License not Registred! Note: Check User ID')
        elif choice == '3':
            print("")
            print("Note: User Menu pops up only after proper registration. Kindly Login Up incase Registred Already!")
            mainMenu()
        else:
            print('Invalid option !')

def userMenu(current_user):
    choice = -1

    while choice != '7':
        print('\n')
        print('1.Change Address')
        print('2.Generate Vehicle Temporary No.')  
        print('3.Transfer Vehicle Registration')                      
        print('4.Sale Transactions Records')
        print('5.Change Vehicle Details')
        print('6.Change Add License Information')
        print('7.Email : User Personal, Vehicle, License Details')
        print('8.Logout')
        choice = input('Enter your choice: ')
        if choice == '1':
            address = input('Address: ').upper()
            city = input('City: ').upper()
            state = input('State: ').upper()
            pincode = int(input('Pincode: '))
            query = "UPDATE account_holder_details SET address = %s, city = %s, state = %s, pincode = %s where user_id=%s "
            cur = db.getCursor()
            if cur.execute(query, (address, city, state, pincode,current_user)):
                db.commit()
                print("")
                print('Address was updated!')
            else:
                print('Address could not be updated')
        if choice == '2':
            user_id = input('User id (Case-Sensitive): ')
            password = input('Password : ')
        
            vname = input('Vehicle Name :').upper()
            vtype = input('Vehicle Type (2/4 Wheeler) :').upper()
            vmodel = input('Vehicle Model :').upper()
            vprice = input('Vehicle Price :').upper()
            vowner = input('Vehicle Owner Name :').upper()
            new_number = Number(user_id, vname, vtype, vmodel, vprice, vowner)
            
            
            if ((User.authenticate(user_id,password)) and (new_number.save())):
                print("")
                print('Your temporary no. generated successfully!')
                print("")
                random = temp()
                random.gen()
                     
               
            else:
                print('Not Generated')
                
                     
            
                
             
        elif choice == '3':
            user_id = input('User id (Case-Sensitive): ')
            password = input('Password : ')
                    
            vyear = int(input('Vehicle Sale Year :'))
            vnumber = input('Vehicle Number :').upper()
            vnowner = input('Vehicle New Owner Name :').upper()
            vprice = input('Vehicle Sale Price :').upper()
            vpowner = input('No. of Vehicle Previous Owners :').upper()
            vtype = input('Vehicle Type (2/4 Wheeler): ').upper()
            new_transfer = transfer(user_id, vyear, vnumber, vnowner, vprice, vpowner, vtype)
            if((User.authenticate(user_id,password)) and (new_transfer.save())):
                print("")
                print('Your Vehicle Got Transferred to {}!'.format(vnowner))
                Task.active(user_id)
                
            else:
                print('Not Transferred !')
        elif choice == '4':
            user_id = input('Enter User id (Case-Sensitive): ')
            print("")
            stataccount = Task.getStataccount(user_id)
            for statement in stataccount:
                print("Personal User Information:")
                print("First Name | Last Name | Address | City | State")
                print(str(statement[0]) + "|" + str(statement[1]) + "|" + str(statement[5]) + "|" + str(statement[6]) + "|" + str(statement[7]))
                print("")
            statvehicle = Task.getStatvehicle(user_id)
            for stat in statvehicle:
                print("Vehicle Details:")
                print("Vehicle No. | Vehicle Name | Vehicle Type(2/4) | Vehicle Year | Vehicle Owner | Vehicle State")
                print(str(stat[1]) + "|" + str(stat[3]) + "|" + str(stat[2]) + "|" + str(stat[7]) + "|" + str(stat[6]) + "|" + str(stat[8]))
                print("")
            stattransfer = Task.getStattransfer(user_id)
            for state in stattransfer:
                print("Vehicle Transfer Details:")
                print("Vehice Sale Year | Vehicle Number | Vehicle New Owner | Vehicle Sale Price | No. of Previous Owners")
                print(str(state[1]) + "|" + str(state[2]) + "|" + str(state[3]) + "|" + str(state[4]) + "|" + str(state[5]))
            
        elif choice == '5':
            vehicle_no = input('Vehicle No.: ').upper()
            vehicle_type = input('Vehicle Type (2/4 Wheeler): ').upper()
            vehicle_name = input('Vehicle Name: ').upper()
            vehicle_model = input('Vehicle Model: ').upper()
            vehicle_color = input('Vehicle Color: ').upper()
            vehicle_owner = input('Vehicle Owner Name: ').upper()
            vehicle_year = int(input('Vehicle Purchase Year: '))
            query = "UPDATE vehicle_details SET vehicle_no = %s, vehicle_type = %s, vehicle_name = %s, vehicle_model = %s, vehicle_color = %s, vehicle_owner = %s, vehicle_year = %s where user_id=%s "
            cur = db.getCursor()
            if cur.execute(query, (vehicle_no, vehicle_type, vehicle_name, vehicle_model, vehicle_color, vehicle_owner, vehicle_year,current_user)):
                db.commit()
                print("")
                print('Vehicle Details was updated!')
            else:
                print('Vehilce Deatils could not be updated')
                
        elif choice == '6': 
            license_no = input('Enter your License no.: ').upper()
            driver_name = input('Enter Driver Name: ').upper()
            issue_year = int(input('Issued Year: '))
            expire_year = int(input('Expire Year (Valid Upto): '))
            issue_authority = input('Issue Authority: ').upper()
            vehicle_type = input('Vehicle Type (2/4 Wheeler): ').upper()
            query = "UPDATE license_details SET license_no = %s, driver_name = %s, issue_year = %s, expire_year = %s, issue_authority = %s, vehicle_type = %s where user_id=%s "
            cur = db.getCursor()
            if cur.execute(query, (license_no, driver_name, issue_year, expire_year, issue_authority, vehicle_type,current_user)):
                db.commit()
                print("")
                print('License Information was updated!')
            else:
                print('License Information could not be updated')
           
        elif choice == '7': 
            print("")
            print("Note: Enter Your User id - Information Mail attached to ID will be sent!")
            print("")
            user_id = input('Enter User id (Case-Sensitive): ')
            email_id = input('Enter Email-ID: ')
            details_email.getmail(user_id,email_id)
        elif choice == '8':
            mainMenu()
        else:
            print('Invalid option!')

def adminMenu():
    choice = -1

    while choice != '6':
        print('\n')
        print('1.View all Personal Account Information')
        print('2.View all Registred Vehicle List')
        print('3.View all Valid Licensed Drivers') 
        print('4.Search Engine')
        print('5.Email : User Personal, Vehicle, License Details')
        print('6.Admin Logout')

        choice = input('Enter your choice: ')
        if choice == '1':
            full_details = fullaccount()
            full_details.full()
        elif choice == '2':
            ful = fullvehicle()
            ful.fully()
        elif choice == '3':
            fuli = fulllicense()
            fuli.ful()   
        elif choice == '4':
            print("1. List all User ID's")
            print("2. Search Information by User ID")
            print("")
            choice = input('Enter your choice: ')
            if choice == '1':
                print("")
                query = "SELECT user_id from account_holder_details"
                cur = db.getCursor()
                cur.execute(query)
                result =  cur.fetchall()
                for i in result:
                     print (i)
            elif choice == '2':
                choice = -1
                user_id = input('Enter User id (Case-Sensitive): ')
                print("")
                stataccount = Task.getStataccount(user_id)
                for statement in stataccount:
                    print("Personal User Information:")
                    print("First Name | Last Name | Address | City | State")
                    print(str(statement[0]) + "|" + str(statement[1]) + "|" + str(statement[5]) + "|" + str(statement[6]) + "|" + str(statement[7]))
                    print("")
                statvehicle = Task.getStatvehicle(user_id)
                for stat in statvehicle:
                    print("Vehicle Information:")
                    print("Vehicle No. | Vehicle Name | Vehicle Type(2/4) | Vehicle Year | Vehicle Owner | Vehicle State")
                    print(str(stat[1]) + "|" + str(stat[3]) + "|" + str(stat[2]) + "|" + str(stat[7]) + "|" + str(stat[6]) + "|" + str(stat[8]))
                    print("")
                statlicense = Task.getStatlicense(user_id)
                for st in statlicense:
                    print("Driver License Information:")
                    print("Driver License No. | Driver Name | Vehicle Type | Issue Year | Expire Year | Issue Authority")
                    print(str(st[0]) + "|" + str(st[2]) + "|" + str(st[6]) + "|" + str(st[3]) + "|" + str(st[4]) + "|" + str(st[5]))
                    print("")
                stattransfer = Task.getStattransfer(user_id)
                for state in stattransfer:
                    print("Transfer Information:")
                    print("Vehice Sale Year | Vehicle Number | Vehicle New Owner | Vehicle Sale Price | No. of Previous Owners")
                    print(str(state[1]) + "|" + str(state[2]) + "|" + str(state[3]) + "|" + str(state[4]) + "|" + str(state[5]))
            else:
                print('Invalid option !')
        elif choice == '5': 
            print("")
            print("Note: Enter Desired User id - Information Mail attached to User-ID will be sent!")
            print("")
            user_id = input('Enter User id (Case-Sensitive): ')
            email_id = input('Enter Email-ID: ')
            details_email.getmail(user_id,email_id)
        elif choice == '6':
            mainMenu()
        else:
            print('Invalid option !')

def mainMenu():
    logo = ''' ******************* WELCOME TO RARS - rtovehicle.ooo ****************
               
       *************** AUTOMOBILE REGSITRATION SYSTEM  ***********
            
          ************* MAKE SURE THAT INTERNET IS WORKING *********** '''

    print(logo)
    choice  = -1    
    current_user = -1

    while choice != '4':
        print('\n')
        print('1.Sign Up')
        print('2.Login Up')
        print('3.Admin Sign In')
        print('4.Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            first_name = input('First Name: ').upper()
            last_name = input('Last Name: ').upper()
            user_id = input('User id (Case-Sensitive): ')
            while True:
                password = input('Password (Min. 6-12 Digit): ')
                if 6 <= len(password) < 12:
                    break
                print("")
                print ('The password must be between 6 and 12 characters.\n')            
            address = input('Enter Address: ').upper()
            city = input('City: ').upper()
            state = input('State: ').upper()
            pincode = int(input('Pincode: '))
            phone = int(input('Phone No.: '))
			hash = 
            new_user = User(first_name, last_name,user_id, password, address, city, state, pincode, phone)
            
            if new_user.save():
                print("")
                print('Thanks for signing up!')
                current_user = user_id
                accountMenu(current_user);
            else:
                print('Cannot create an account for you')
                
        elif choice == '2':
            attempts = 1
            while attempts <=3:
                print("")
                print("Attempt %d: "%(attempts))
                user_id = input('User id (Case-Sensitive): ')
                password = input('Password: ')

                if (User.authenticate(user_id,password)):
                    current_user = user_id
                    userMenu(current_user);
                    break            
                else:
                    print('Invalid credentials!')
                attempts += 1
            else:
                print('Max sign in attempts reached')
        elif choice == '3':
            attempts = 1
            while attempts <=3:
                print("")
                print("Attempt %d: "%(attempts))
                username = input('Admin Userid: ')
                password = input('Password: ')
                if Admin.authenticate(username, password):
                    adminMenu();                    
                    break            
                else:
                    print('Invalid credentials!')
                attempts += 1
            else:
                print('Max sign in attempts reached')
        elif choice == '4':
            exit()
        else:
            print('Invalid option!')
    


class temp:
                def gen(self):
                 N=9
                 m=1
                 characters = string.ascii_uppercase + string.digits 
                 no =  "".join(choice(characters) for x in range(N))
                 s = ('-'*m).join(no)
                 print (s)
        
class fullaccount:
            def full(self):
                 sql = "SELECT * FROM account_holder_details"
                 cur = db.getCursor()
                 cur.execute(sql)
                 db.commit()
                 results = cur.fetchall()

                 widths = []
                 columns = []
                 tavnit = '|'
                 separator = '+' 

                 for cd in cur.description:
                         
                         widths.append(max(cd[2], len(cd[0])))
                         columns.append(cd[0])

                 for w in widths:
                     tavnit += " %-"+"%s.%ss |" % (w,w)
                     separator += '-'*w + '--+'

                     
                     
                 for row in results:
                     print(separator)
                     print(tavnit % row)
                     print(separator)
                     
class fullvehicle:
            def fully(self):
                 sql = "SELECT * FROM vehicle_details"
                 cur = db.getCursor()
                 cur.execute(sql)
                 db.commit()
                 results = cur.fetchall()

                 widths = []
                 columns = []
                 tavnit = '|'
                 separator = '+' 

                 for cd in cur.description:
                         
                         widths.append(max(cd[2], len(cd[0])))
                         columns.append(cd[0])

                 for w in widths:
                     tavnit += " %-"+"%s.%ss |" % (w,w)
                     separator += '-'*w + '--+'

                     
                     
                 for row in results:
                     print(separator)
                     print(tavnit % row)
                     print(separator)  
                     
class fulllicense:
            def ful(self):
                 sql = "SELECT * FROM license_details"
                 cur = db.getCursor()
                 cur.execute(sql)
                 db.commit()
                 results = cur.fetchall()

                 widths = []
                 columns = []
                 tavnit = '|'
                 separator = '+' 

                 for cd in cur.description:
                         
                         widths.append(max(cd[2], len(cd[0])))
                         columns.append(cd[0])

                 for w in widths:
                     tavnit += " %-"+"%s.%ss |" % (w,w)
                     separator += '-'*w + '--+'

                     
                     
                 for row in results:
                     print(separator)
                     print(tavnit % row)
                     print(separator) 
# display main menu                 
mainMenu();

