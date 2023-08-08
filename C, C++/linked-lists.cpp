//Kyle A. Destura || BSCS 2-B
//Implementation of linkedlists..

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

struct PhoneNode{
    int unitNumber;
    string brandName;
    string modelCode;
    double price;
    PhoneNode *nextPtr;
    PhoneNode *prevPtr;

}*headNode = NULL, *tailNode = NULL;  //Initialize all to null.


void displayList();
PhoneNode* createNode();
void insertUnit();
void insertUnitAt();
void moveToHead();
void moveToTail();
void deleteUnit();




int main() {

    for(int i = 0; i < 15; i++)
        insertUnit();

    displayList();

    insertUnitAt();
    displayList();

    moveToHead();
    displayList();

    moveToTail();
    displayList();

    deleteUnit();
    displayList();

    deleteUnit();
    deleteUnit();
    deleteUnit();
    displayList();

    return 0;
}




//Function displayList(): displays all the node in the list
void displayList() {

    if(headNode != NULL) {  //If not empty list, proceed to print
        PhoneNode *currentNode = headNode;

        while(currentNode != NULL) {
            cout << "Unit Number\t : " << currentNode->unitNumber << "\n";
            cout << "Brand Name \t : " << currentNode->brandName << "\n";
            cout << "Mode Code  \t : " << currentNode->modelCode << "\n";
            cout << "Price      \t : " << currentNode->price << "\n\n";
            currentNode = currentNode->nextPtr;
        }

    } else
        cout << "There is nothing in the list.\n";

}





//Function createNode(): creates a node then returns it
PhoneNode* createNode() {

    PhoneNode *newNode = new(PhoneNode);

    if(headNode == NULL)
        cout << "Unit Number: 1\n";
    else
        cout << "Unit Number: " << tailNode->unitNumber+1 << "\n";


    cout << "Brand Name: ";
    string brandName;
    getline(cin, brandName);
    newNode->brandName = brandName;

    cout << "Model Code: ";
    string modelCode;
    getline(cin, modelCode);
    newNode->modelCode = modelCode;

    cout << "Price: ";
    double price;
    cin >> price;
    cin.ignore();
    newNode->price = price;

    newNode->nextPtr = NULL;

    cout << "\n";
}





//Function insertUnit(): Adds a node at the last node
void insertUnit() {

    PhoneNode *newNode = createNode();

    if(headNode == NULL) {  //If it is the first node, make it the head.
        headNode = newNode;
        tailNode = headNode;       //also point the tailNode to the head since there is only 1 in the list
        headNode->unitNumber = 1;

    } else {
        newNode->unitNumber = tailNode->unitNumber+1;
        tailNode->nextPtr = newNode;
        tailNode = newNode;         //Make the new node the tail node
    }

}





//Function to insert unit at custom position
//Did not implement if position is at head node or the previous node of tail node since it was not in the requirements and will make the code longer..
void insertUnitAt() {

    PhoneNode *currentNode = headNode;
    PhoneNode *newNode = createNode();
    newNode->unitNumber = tailNode->unitNumber+1;

    int unitNumber;
    cout << "Insert at Unit: ";
    cin >> unitNumber;
    cin.ignore();


    if(unitNumber < 1) {
        cout << "Error inputted position. should be greater than 0.\n";
        return;

    } else {

        currentNode = headNode;
        for(int i = 1; i < unitNumber; i++)     //Stop traversing at the preceeding node of the targeted node
            currentNode = currentNode->nextPtr;

        cout << "Inserting between Unit " << currentNode->unitNumber << " and Unit " << currentNode->nextPtr->unitNumber << "\n";


        newNode->nextPtr = currentNode->nextPtr;
        currentNode->nextPtr = newNode;
    }

}




//Did not implement if position is at tail node or the next node of head node since it was not in the requirements and will make the code longer..
//Function move a node to the head
void moveToHead() {

    int unitNumber;
    cout << "Moving unit at the beginning of the list.\n";
    cout << "Unit Number to be moved: ";
    cin >> unitNumber;
    cin.ignore();

    PhoneNode *currentNode = headNode;

    if(unitNumber < 1) {

        cout << "Error inputted position. Will not be moved.\n";
        return;

    } else {

        currentNode = headNode;
        for(int i = 1; i < unitNumber-1; i++)     //Stop traversing at the preceeding node of the targeted node
            currentNode = currentNode->nextPtr;

        PhoneNode *tempNode = currentNode->nextPtr;
        currentNode->nextPtr = currentNode->nextPtr->nextPtr;
        tempNode->nextPtr = headNode;
        headNode = tempNode;
    }
}




//Did not implement if position is at head node or the previous node of tail node since it was not in the requirements and will make the code longer..
//Function that moves a node to the tail
void moveToTail() {

    int unitNumber;
    cout << "Moving unit at the end of the list.\n";
    cout << "Unit Number to be moved: ";
    cin >> unitNumber;
    cin.ignore();

    PhoneNode *currentNode = headNode;

    if(unitNumber < 1) {

        cout << "Error inputted position. Will not be moved.\n";
        return;

    } else {

        currentNode = headNode;
        for(int i = 1; i < unitNumber-1; i++)     //Stop traversing at the preceeding node of the targeted node
            currentNode = currentNode->nextPtr;

        PhoneNode *tempNode = currentNode->nextPtr;
        currentNode->nextPtr = tempNode->nextPtr;

        tailNode->nextPtr = tempNode;
        tailNode = tempNode;
        tailNode->nextPtr = NULL;

    }

}




//Did not implement if position is at head node or tail node since it was not in the requirements and will make the code longer..
//Function that deletes a node from the list
void deleteUnit() {

    int unitNumber;
    cout << "Deleting a unit...\n";
    cout << "Unit Number to be deleted: ";
    cin >> unitNumber;
    cin.ignore();

    PhoneNode *currentNode = headNode;

    if(unitNumber < 1) {
        cout << "Error input. should be greater than 0.\n";
        return;

    } else {
        currentNode = headNode;
        bool isFound = false;
        while(currentNode != NULL) { //Stop at the preceeding node of the targeted node and stop at NULL

            if(currentNode->nextPtr->unitNumber == unitNumber) {
                isFound = true;
                break;
            }

            currentNode = currentNode->nextPtr;

        }

        PhoneNode *tempNode = currentNode->nextPtr;     //set temporary so that it can be deleted
        currentNode->nextPtr = tempNode->nextPtr;
        delete tempNode;
    }
}
