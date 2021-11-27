/* Algo.h contains the implementation for the IDS and A* search algorithm */

#ifndef Algorithm
#define Algorithm

#include <list>
#include <iterator>
#include "Node.h"

using namespace std;

class Search {
public:

    int expandedNodes = 0; //For tracking how many nodes are opened

    Search() {
        expandedNodes = 0;
    } 

    list<Node> IterativeDeepeningSearch(Node root) {
        
        list<Node> pathToSolution;

        bool goalFound = false;
        int depthLimit = 0; 

        while(!goalFound) { //from depth 1 to infinity till goal is found

            list<Node> openList; 
            list<Node> closedList; 

            openList.push_back(root);
            depthLimit++;

            while((openList.size() > 0) && !goalFound) {

                //stack implementation
                Node *currentNode = new Node(openList.back());    
                this->expandedNodes++;  
                closedList.push_back(*currentNode); 
                openList.pop_back();
                
                currentNode->expandNode();

                //iterate through list of the expanded nodes
                for(list<Node>::iterator currentChild = currentNode->children.begin(); currentChild != currentNode->children.end(); currentChild++) {
                    
                    //if current node is below limit and is unique, add it to open list
                    if( getDepth(*currentChild) < depthLimit ) {    
                        if( !(contains(openList, *currentChild)) && !(contains(closedList, *currentChild)) ) 
                            openList.push_back(*currentChild);

                    //if it is at the limit then apply goal test
                    } else if(currentChild->goalTest()) {   
                            goalFound = true;
                            pathToSolution = pathTrace(*currentChild);
                            return pathToSolution;
                    }   

                }
            }
        }
            
        return pathToSolution;
    }

//AStarSearch
    list<Node> AStarSearch(Node root) { 

        list<Node> pathToSolution;
        list<Node> openList; 
        list<Node> closedList; 

        openList.push_back(root);
        root.fValue = root.manhattanDistance(); //since it is the root, there is no g(n) yet

        bool goalFound = false;

        while(!goalFound && openList.size() > 0) {

            Node *minNode = new Node();  //for storing of the node wit minimum f value
            int minF = 9999;  //for comparison, just a basic compare
            int minFIndex = 0;
            int removeIndex = 0;    //for removing node from open or closed list
            list<Node>::iterator remove = openList.begin(); // for removing an element from the list

            /* For taking the state with the least f(n) */
            for(list<Node>::iterator currentNode = openList.begin(); currentNode != openList.end(); currentNode++) {
                
                int currentF = currentNode->fValue;

                if(currentNode->goalTest()) {   //to check if it the goal to avoid overlapping
                    goalFound = true;
                    pathToSolution = pathTrace(*currentNode);
                    return pathToSolution;
                }

                if(currentF < minF) {   //linear search for state with least f value
                    minF = currentF;
                    *minNode = *currentNode;
                    minFIndex = removeIndex;
                }

                removeIndex++;
            }

            closedList.push_back(*minNode); 
            this->expandedNodes++; 

            advance(remove, minFIndex);
            openList.erase(remove);

            minNode->expandNode();

            if(minNode->children.size() > 0) {

                for(list<Node>::iterator currentChild = minNode->children.begin(); currentChild != minNode->children.end(); currentChild++) {
                    //for calculating the f(n) value
                    currentChild->fValue = getDepth(*currentChild) + currentChild->manhattanDistance() - 1;
                    //checks if it is a unique node
                    if( !(contains(openList, *currentChild)) && !(contains(closedList, *currentChild)) ) 
                        openList.push_back(*currentChild);
                    
                    else {
                        //if it is not a unique node, check if its f value is lower than the node in the open list
                        removeIndex = 0;
                        for(list<Node>::iterator it = openList.begin(); it != openList.end(); it++) {
                            if( it->isSamePuzzle(currentChild->puzzle) && currentChild->fValue < it->fValue ) {   
                                    openList.push_back(*currentChild);  //put it in the open list
                                    
                                    remove = openList.begin();  //a very tiring way of removing a node from a list
                                    advance(remove, removeIndex);
                                    openList.erase(it);

                                    break;
                            }
                            removeIndex++;
                        }
                        //if it is not a unique node, check if its f value is lower than the node in the closed list
                        removeIndex = 0;
                        for(list<Node>::iterator it = closedList.begin(); it != closedList.end(); it++) {

                            if( it->isSamePuzzle(currentChild->puzzle) && currentChild->fValue < it->fValue ) {
                                    openList.push_back(*currentChild); 

                                    remove = openList.begin(); //another very tiring way of removing a node from a list
                                    advance(remove, removeIndex);
                                    closedList.erase(remove);

                                    break;
                            }
                            removeIndex++;
                        }

                    }
                }

            } else 
                return pathToSolution;
        }

        openList.clear();
        closedList.clear();

        return pathToSolution;
    }

    int getDepth(Node n) {

        int depth = 0;
        Node currentNode = n;

        while(currentNode.parent != NULL) { 
            currentNode = *currentNode.parent;
            depth++;
        }
        return depth;
    }

    list <Node> pathTrace(Node n) {

        list<Node> path;
        Node currentNode = n;
        path.push_front(currentNode);

        while(currentNode.parent != NULL) { 
            currentNode = *currentNode.parent;
            path.push_front(currentNode);
        }
        return path;
    }

    static bool contains(list<Node> tempList, Node x) {

        bool contains = false;
        for(list<Node>::iterator it = tempList.begin(); it != tempList.end(); it++) {
            if(it->isSamePuzzle(x.puzzle)) 
                contains = true;
        }
        return contains;
    }   
    
//end of algorithm
};

#endif 


