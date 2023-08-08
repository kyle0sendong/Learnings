//Code can Add, Remove, Edit, Display all Info, Display all Names in the Database...
//Personal Information includes : Name, Sex, Date of Birth, Address, Civil Status, Phone Number and E-mail Address

#include<bits/stdc++.h> //for converting string to uppercase and sort method
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct employeeInfo {
    string firstName;
    string middleName;
    string lastName;
    string fullName;
    string sex;
    string civilStatus;
    string birthdate;
    string address;
    string phoneNumber;
    string emailAddress;
};

//functions used in the menu.
void addEmployee(employeeInfo employee[]);    //Add employee, inside determines a vacant slot available, and some error check..
void removeEmployee(employeeInfo employee[]);     //Removes an employee, fills the info with empty string then stores the index to Vacant Slot array..
void displayEmployeeInfo(employeeInfo employee[]);    //Displays all the information of the Employee..
void editEmployee(employeeInfo employee[]);     // Edits User info
void displayAllEmployeeNames(employeeInfo employee[]); //Displays all the names in the database

//functions used in the menu functions and also to decrease code duplication
void displayOptions();  //Displays the option...
void loadCSV(employeeInfo employee[]); //Loads the CSV file (employees.csv) at the beginning of the main function
void saveAsCSV(employeeInfo employee[]); //Saves the current database to a employees.csv
int searchEmployee(employeeInfo employee[], string fullName);   //Returns the index of the searched employee name
void setEmployeeInfo(employeeInfo employee[], int position, string firstName, string middleName, string lastName);    //sets other information on the struct...
string enterFullName();  //Asks for the full name then convert to uppercase, returns the full name entered by the user in uppercase
string nameToFullName(string firstName, string middleName, string lastName);    //Returns a converted uppercased full name

int vacantSlot[99];    //This is where the index of a removed employee is stored.
int removedEmployeeCounter = 0;     //Serves as a counter if there is a vacant slot available to be filled up
int currentCompanySize = 0; //Used for tracking the company size, also as an index for the struct array



int main() {

    struct employeeInfo employee[100];
    bool quit = false;
    loadCSV(employee);
    displayOptions();

    while(!quit) {
        string choice;     //Only the first Char is used as the choice
        cout << "\nSelect Activity: ";
        getline(cin, choice);

        switch(choice[0]) {
            case '0': {
                cout << "Saving and Exitting...\n";
                saveAsCSV(employee);
                quit = true;
                break;
            }

            case '1': {
                   if((currentCompanySize-removedEmployeeCounter) < 100){       //Condition when the database is already full..
                        addEmployee(employee);
                        break;
                   } else {
                        cout << "Company is not hiring as of the moment.\n";
                        break;
                   }
            }

            case '2':
                removeEmployee(employee);
                break;

            case '3':
                editEmployee(employee);
                break;

            case '4':
                displayEmployeeInfo(employee);
                break;

            case '5':
                cout << "Displaying all Employee in the company...\n";
                displayAllEmployeeNames(employee);
                break;

            case '6':
                displayOptions();
                break;

            default:
                cout << "Please enter correct Menu option.\n";
                break;
        }
    }

    return 0;
}



//-------------------Menu functions---------------------

void addEmployee(employeeInfo employee[]) {

    string firstName, middleName, lastName;

    cout << "Enter First Name: ";
    getline(cin, firstName);
    cout << "Enter Middle Name: ";
    getline(cin, middleName);
    cout << "Enter Last Name: ";
    getline(cin, lastName);

    string fullName = nameToFullName(firstName, middleName, lastName);

    if(removedEmployeeCounter > 0) {    //Checks if vacant slot available

        if(searchEmployee(employee, fullName) < 0) {     //Checks if employee already exist.

            int i = vacantSlot[removedEmployeeCounter-1];   //Fills up the vacant slot with new info
            setEmployeeInfo(employee, i, firstName, middleName, lastName);
            removedEmployeeCounter--;
            cout << "Added Employee: " << fullName << "\n";

        } else
            cout << "Employee: " << fullName << " already exist\n";

    } else { //Fill up a new slot when no vacant slot available..

        if(searchEmployee(employee, fullName) < 0) {
            currentCompanySize++;
            setEmployeeInfo(employee, currentCompanySize-1, firstName, middleName, lastName);
            cout << "Added Employee: " << fullName << "\n";

        } else
            cout << "Employee: " << fullName << " already exist\n";

    }
}



void removeEmployee(employeeInfo employee[]) {

    cout << "Removing an Employee...\n" << "Enter Name: ";
    string fullName = enterFullName();
    int position = searchEmployee(employee, fullName);

    if(position >= 0) {     //Checks if employee exist.

        removedEmployeeCounter++;      //Adds 1 to the counter of removed employee
        vacantSlot[removedEmployeeCounter-1] = position;    //Stores the index of removed employee

        //Sorts the vacant slot in reverse order for filling up vacant slots or skipping vacant slots
        sort(vacantSlot, vacantSlot+removedEmployeeCounter, greater<int>());

        //Sets everything to empty string on the info of the removed employee
        employee[position].firstName = "";
        employee[position].middleName = "";
        employee[position].lastName = "";
        employee[position].fullName = "";
        employee[position].sex = "";
        employee[position].address = "";
        employee[position].civilStatus = "";
        employee[position].birthdate = "";
        employee[position].phoneNumber = "";
        employee[position].emailAddress = "";

        cout << "Employee: " << fullName << " removed successfully\n";

    } else
        cout << "Employee: " << fullName << " does not exist.\n";

}



void displayEmployeeInfo(employeeInfo employee[]) {    //Displays all the info of the employee...
    cout << "Display Employee Information...\n" << "Enter Name: ";
    string fullName = enterFullName();
    int position = searchEmployee(employee, fullName);

    if(position >= 0) {
        cout << "\nName : " << employee[position].fullName << "\n";
        cout << "Sex : " << employee[position].sex << "\n";
        cout << "Date of Birth : " << employee[position].birthdate << "\n";
        cout << "Address : " << employee[position].address << "\n";
        cout << "Civil status : " << employee[position].civilStatus << "\n";
        cout << "Phone Number : " << employee[position].phoneNumber << "\n";
        cout << "E-mail Address : " << employee[position].emailAddress << "\n";

    } else
        cout << "Employee: " << fullName << " does not exist.\n";
}



void editEmployee(employeeInfo employee[]) {          //edit the employee's name, civil status or address.

    cout << "Editing an Employee...\n" << "Enter Name: ";
    string fullName = enterFullName();
    int position = searchEmployee(employee, fullName);

    if(position >= 0) { //Check if employee exist.

        cout << "Which info do you want to edit? \n[1]Name \n[2]Sex \n[3]Date of Birth \n[4]Address \n[5]Civil Status  \n[6]Phone Number \n[7]E-mail Address \n[0]Cancel\n";
        string choice;  //First character is only read..
        cout << "Choice: ";
        getline(cin, choice);

        switch(choice[0]) {

            case '1': {
                    string firstName, middleName, lastName;
                    cout << "Enter First Name: ";
                    getline(cin, firstName);
                    cout << "Enter Middle Name: ";
                    getline(cin, middleName);
                    cout << "Enter Last Name: ";
                    getline(cin, lastName);

                    string fullName = nameToFullName(firstName, middleName, lastName);      //get the uppercased full name

                    if(searchEmployee(employee, fullName) >= 0) {  //Check if new edited name already exist...
                        cout << "Employee: " << fullName << " already exist. Cancelling operation\n";
                        return;

                    } else {
                        employee[position].firstName = firstName;
                        employee[position].middleName = middleName;
                        employee[position].lastName = lastName;
                        employee[position].fullName = fullName;
                    }
                    break;
            }

            case '2':
                    cout << "Enter your new Gender Identity: ";
                    getline(cin, employee[position].sex);
                    break;

            case '3':
                    cout << "Enter your Date of Birth: ";
                    getline(cin, employee[position].birthdate);
                    break;

            case '4':
                    cout << "Enter your new Address: ";
                    getline(cin, employee[position].address);
                    break;

            case '5':
                    cout << "Enter your new Civil Status: ";
                    getline(cin, employee[position].civilStatus);
                    break;

            case '6':
                    cout << "Enter your new Phone Number: ";
                    getline(cin, employee[position].phoneNumber);
                    break;

            case '7':
                    cout << "Enter your new E-mail Address: ";
                    getline(cin, employee[position].emailAddress);
                    break;

            case '0':
                    cout << "Cancelled operation.\n";
                    return;     //don't know why return doesn't work here..

            default:
                    cout << "Entered not on the list. Cancelling operation.\n";
                    return;
        }

        cout << "\nEdit successful!\n";

    } else
        cout << "Employee: " << fullName << " does not exist.\n";

}


void displayAllEmployeeNames(employeeInfo employee[]) {

    if((currentCompanySize - removedEmployeeCounter) > 0) {

        int j = removedEmployeeCounter-1;

        for(int i = 0; i < currentCompanySize; i++) {

            if(removedEmployeeCounter > 0)  //if there is a removed employee, skip the vacant slot for displaying...
                if (vacantSlot[j] == i) {
                    j--;
                    continue;
                }

            cout << employee[i].fullName << "\n";
        }

    } else
        cout << "No employee in this Company\n";
}



/*------------ functions used in the menu functions ---------*/

void displayOptions() {

    cout << "\n************************\n";
    cout << "MENU\n";
    cout << "************************\n";
    cout << "0 - Exit and Save\n";
    cout << "1 - Add a record\n";
    cout << "2 - Delete a record\n";
    cout << "3 - Edit a record\n";
    cout << "4 - Search / Display a record\n";
    cout << "5 - Display all employee names in the company\n";
    cout << "6 - Display Menu Options\n";
    cout << "************************\n";
}


void loadCSV(employeeInfo employee[]) {     //loads the csv file

    ifstream myFile("employees.csv");

    if(!myFile.is_open()) {
        cout << "Error! no employees.csv opened.\n";
        return;
    }

    else
        cout << "Loaded employees.csv successfully\n";


    string skip;
    for(int i = 0; i < 8; i++)      //skip the first horizontal
        getline(myFile, skip, ',');

    getline(myFile, skip);


    while(getline(myFile, employee[currentCompanySize].lastName, ',')) { //Ends if no more ',' is found
        int i = currentCompanySize; //Used i instead of currentCompanySize for readability purpose..
        getline(myFile, employee[i].firstName, ',');
        getline(myFile, employee[i].middleName, ',');
        employee[i].fullName = nameToFullName(employee[i].firstName, employee[i].middleName, employee[i].lastName);
        getline(myFile, employee[i].sex, ',');
        getline(myFile, employee[i].birthdate, ',');
        getline(myFile, employee[i].address, ',');
        getline(myFile, employee[i].civilStatus, ',');
        getline(myFile, employee[i].phoneNumber, ',');
        getline(myFile, employee[i].emailAddress);
        currentCompanySize++;
    }

    myFile.close();
}


void saveAsCSV(employeeInfo employee[]) {

    ofstream myFile;
    myFile.open("employees.csv");

    myFile << "Last Name," << "First Name," << "Middle Name," << "Sex," << "Date of Birth," << "Address," << "Civil Status," << "Phone Number," << "E-mail Address\n";

    int j = removedEmployeeCounter-1;
    for(int i = 0; i < currentCompanySize; i++) {

        if(removedEmployeeCounter >= 1) { //Skips the vacant slot in saving, so no empty information are stored
            if (vacantSlot[j] == i) {
                j--;
                continue;
            }
        }

        myFile << employee[i].lastName << "," << employee[i].firstName << "," << employee[i].middleName << ",";
        myFile << employee[i].sex << ",";
        myFile << employee[i].birthdate << ",";
        myFile << employee[i].address << ",";
        myFile << employee[i].civilStatus << ",";
        myFile << employee[i].phoneNumber << ",";
        myFile << employee[i].emailAddress << "\n";
    }

    cout << "\nSaved as employees.csv successfully.\n";
    myFile.close();
}


int searchEmployee(employeeInfo employee[], string fullName) {  //Searches for the employee full name then returns the index when found

    for(int i = 0; i < currentCompanySize; i++) {
        if((employee[i].fullName.compare(fullName) == 0))
            return i;
    }
    return -1; //employee not found
}



void setEmployeeInfo(employeeInfo employee[], int position, string firstName, string middleName, string lastName) {

    employee[position].firstName = firstName;
    employee[position].middleName = middleName;
    employee[position].lastName = lastName;
    employee[position].fullName = nameToFullName(firstName, middleName, lastName);

    cout << "Sex 'Male or Female. If others, specify...' : ";
    getline(cin, employee[position].sex);

    cout << "Civil status : ";
    getline(cin, employee[position].civilStatus);

    cout << "Date of Birth 'mm-dd-yy' : ";
    getline(cin, employee[position].birthdate);

    cout << "Address : ";
    getline(cin, employee[position].address);

    cout << "Phone Number : ";
    getline(cin, employee[position].phoneNumber);

    cout << "Email Address : ";
    getline(cin, employee[position].emailAddress);
}


string enterFullName() {
    string fullName;
    getline(cin, fullName);
    transform(fullName.begin(), fullName.end(), fullName.begin(), ::toupper);
    return fullName;
}


string nameToFullName(string firstName, string middleName, string lastName) { //pass by value so the address of the passed wont be changed..
    firstName.append(" ");
    middleName.append(" ");
    string fullName = firstName.append(middleName.append(lastName));
    transform(fullName.begin(), fullName.end(), fullName.begin(), ::toupper);
    return fullName;
}
