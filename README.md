This is my Phase 3 Project
Startup:
1)Run: pipenvinstall; pipenv shell
2)In the uppermost directory run: python cli.py
This is a CLI so it is ran and viewed in the terminal. 
The first output is the start of a CRUD operations for a hospital doctor/patient/appointment record system.
You can select Look up records(read), Add record (create), Update record (update), and clear records (delete).
Enter the coorisponding number and you will progress to the next screen.
You can also enter 999 to view the dict type requirement
You can return or quit to the previous 'page' at almost every 'page' by entering the corresponding number
On the Read page you can view all instances of either the doctors, patients, or appointments tables by entering the matching number.
On the create page you can add a record of any of the 3 listed models.  It will persist to the back end.  You can then go back to the read 'page' and verify.  I have built in verifications to prevent the user ffrom breaking the application.

On the update page you can do the same thing.  Depending on the table accessed it will list all the instances and you select the one to edit by entering the corresponding id.  Appointments(because there are so many)  Have to be looked up by first and last name.  From there you can update either the date/time or doctor that is being seen

on the delete page you can either clear entire tables, individual tables or clear specific rows
On the delete page you can either clear entire tables, individual tables or clear specific rows. It will ask you to confirm you selection before clearing the database.

I'll go through the files in more detail below:

cli.py is the  file you should run at the topmost directory, this started the cli application.
That will split the file off and run CRUD functions inside the lib/db/functions directory.

In the /lib directory you can use debug.py to depug if you like but I usually add importipdb;ipdb.set_trace() somewhere and then run the cli.py why to debug

helpers.py is a test file.  You write expirement functions or anything you want there

inside lib/db:

The database.py file has creates conversation with the phase3_database.db file.  I imported to all files that needed it as 'session'.
I added code there so a new 'phase3_database.db' file wouldn't be created in other directories.  That way you can run the cli.py file in the topmost directory and it will access the correct db file without creating a blank duplicate

The seed.py file is used to seed the database with random data.  You can edit how many rows/instances are created there on lines 64, 65, and 66

models.py is where I wrote the blueprints for all my tables and designed the relationships.
I also added a dictionary object class so my project included dictionaries.  You can view it in the Read 'page' of the application or run an ipdb session and make your own instance.

phase3_database.db is the database file.  I use the VSCode extension to view it

There is an alembic.ini and /alembic directory for migrations.  There not much use to you because I had a lot of issues at the beginning so there is just one 2 versions.

in the lib/db/functions I have all my CRUD functions build in:

read_functions.py:

This has all the functions to read the database.  Just select the model you want to view and it will print all the rows of its assigned table.

add_functions.py:

add_func_1 is the main Create file.  It will split of to 2,3 and 4. 2 and 3 allow you to create Doctor or Patient rows and 4 allows you to create a new appointment.  
add_func_4 is pretty indepth.  It will verify available doctors on the specific date/time you enter.
All add_funcs will verify the user input as well.
enter_new_appt() verifies the year, month, day, hour, and minute as well as returning a datetime
generate_pat_id() will generate a patient id, it will return the id if entered patient exists or will create the patient and return the id if the entered patient does not exist
avail_drs_on_date() will return a list of doctors that are available at the datetime you pass in.  It will show only doctors that have no appointments on that specific day.  That way no appointments will overlap

update_functions.py:

update_func_1() is the starting function that calls all the rest.  First select the table you want to update.
validate_selected_id() validates and returns the selected id for for updating either Doctor or Patient
update_func_4() is a placeholder it will immediately call update_func_6() because I only coded enough to lookup appointments by patient.
update_func_6()  Will have you enter a patient name (will print all patient names if the user inputs something invalid).  Then it will run a different function depending on if you want to change doctors your seeing (will verify if they are available first) or change the appointment time (will verify).

delete_functions.py:

The application will allow you to select if you want to clear entire tables or by instance.  I tryied to use clear instead of delete in my print statements because the tables will remain their just the data inside is what is getting deleted.
delete_tables() will clear all or a specific table of all its rows
delete_instance() will have the user specify the table first and then will ask for specific id of the row they want deleted.
You should not be locked into deleting something once you make a selection.  If you type anything but 'yes' when it asks you to confirm it will take you back to the first delete_func_1 'page'

That's pretty much it.

If you want to reseed just run python lib/db/seed.py from the top file or whereever you are in the file structure.