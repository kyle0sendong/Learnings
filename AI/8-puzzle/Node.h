/* Node.h is the implementation of the states of the board 
This contains the code necessary to create new states,
and to get the manhattan distance heuristics of each state */

#ifndef EightPuzzle
#define EightPuzzle 

#include <iostream>
#include <list>
#include <iterator>
#include <cstring>
using namespace std;

class Node {
public: 

    Node *parent;   //also necessary for backtracking of solution path
    list <Node> children;   //for the new states after expanding
    
    int puzzle[9];   //Represented the board in 1D for simplicity
    int column = 3;  //for constraints in moves
    int fValue;      //f(n) of every state

    char moves[10]; //for the required output, "right" "left" "up" "down"

    Node() {}
    Node(int p[]) {   

        setPuzzle(p);
        parent = NULL;
        fValue = 0;
        strcpy(this->moves, "");
    }

    void setPuzzle(int p[]) {   

        for(int i = 0; i < 9; i++) 
            this->puzzle[i] = p[i];
    }

    void printPuzzle() {  

        cout << "\n";
        for(int i = 0, k = 0; i < 3; i++) {

            for(int j = 0; j < 3; j++) {

                if(this->puzzle[k] == 0)
                    cout << "  ";
                else 
                    cout << this->puzzle[k] << " ";

                k++;
            }
            cout << "\n";
        }
    }

    bool isSamePuzzle(int p[]) {

        for(int i = 0; i < 9; i++) 
            if(this->puzzle[i] != p[i])
                return false;

        return true;
    } 

    bool goalTest() {  //I am only using a 1D matrix, I thought it would make it simple :(

        int goal[9] = {1, 2, 3,
                       8, 0, 4,
                       7, 6, 5};
        
        for(int i = 0; i < 9; i++) 
            if(this->puzzle[i] != goal[i])
                return false;
        
        return true;
    }


//legal moves for the nodes, moveRight, moveLeft, moveUp, moveDown

    void expandNode() { //applying the moves to the current node

        int blankTile = -1;

        for(int i = 0; i < 9; i++)    
            if(this->puzzle[i] == 0) 
                blankTile = i;
            
        moveRight(this->puzzle, blankTile);
        moveLeft(this->puzzle, blankTile);
        moveUp(this->puzzle, blankTile);
        moveDown(this->puzzle, blankTile);
    }

    void moveRight(int p[], int i) {
        
        if(i % column < column - 1) {   //constraints of possible move
            int possibleMove[9];
            copyPuzzle(possibleMove, p);

            int temp = possibleMove[i + 1];          //swapping of numbers
            possibleMove[i + 1] = possibleMove[i];   //blank tile to the right
            possibleMove[i] = temp;

            Node *child = new Node(possibleMove);   //make the successful swap a new state
            strcpy(child->moves, "Right");          
            child->parent = this;
            this->children.push_back(*child);
        }
    }

    void moveLeft(int p[], int i) {

        if(i % column > 0) {
            int possibleMove[9];
            copyPuzzle(possibleMove, p);

            int temp = possibleMove[i - 1];
            possibleMove[i - 1] = possibleMove[i];
            possibleMove[i] = temp;

            Node *child = new Node(possibleMove);
            strcpy(child->moves, "Left");
            child->parent = this;
            this->children.push_back(*child);
        }
    }

    void moveUp(int p[], int i) {

        if(i - column >= 0) {
            int possibleMove[9];
            copyPuzzle(possibleMove, p);

            int temp = possibleMove[i - 3];
            possibleMove[i - 3] = possibleMove[i];
            possibleMove[i] = temp;

            Node *child = new Node(possibleMove);
            strcpy(child->moves, "Up");
            child->parent = this;
            this->children.push_back(*child);
        }
    }

    void moveDown(int p[], int i) {

        if(i + column < 9) {
            int possibleMove[9];
            copyPuzzle(possibleMove, p);

            int temp = possibleMove[i + 3];
            possibleMove[i + 3] = possibleMove[i];
            possibleMove[i] = temp;

            Node *child = new Node(possibleMove);
            strcpy(child->moves, "Down");
            child->parent = this;
            this->children.push_back(*child);
        }
    }

    void copyPuzzle(int a[], int b[]) { //used in the possible moves functions

        for(int i = 0; i < 9; i++) 
            a[i] = b[i];
    }
//* end of legal move methods *//

    
//------ for the A* implementation Manhattan Distance -----------//
/* manhattan distance : abs(x - x of goal) + abs(y - y of Goal) */
    int manhattanDistance() { 
        
        int distance = 0;       
        int goalIndex = 0;
        int x = 0;
        int y = 0;
        int xGoal = 0;
        int yGoal = 0;
         
        for(int i = 0; i < 9; i++) 
            if(this->puzzle[i] != i) {
                
                goalIndex = getGoalpos(this->puzzle[i]);  
                x = getXpos(i);
                y = getYpos(i);
                xGoal = getXpos(goalIndex);
                yGoal = getYpos(goalIndex);
                distance += abs(x - xGoal) + abs(y - yGoal);
                
            }
        
        return distance;
    }

    int getGoalpos(int num) {   //takes the goal position of the misplaced tile

        int index = 0;
        int goal[] = {1, 2, 3, 8, 0, 4, 7, 6, 5};

        for(int i = 0; i < 9; i++) 
            if(num == goal[i])
                index = i;
        
        return index;
    }

    int getXpos(int x) {
        return x/3;
    }

    int getYpos(int y) {
        return y % 3;
    }
    

/*End of Node class*/
};


#endif 


