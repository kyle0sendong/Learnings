/* Kyle A. Destura
   BSCS 3-C
  		       Artificial Intelligence
   Solving 8-puzzle problem using IDS and A* search */

#include "Node.h"
#include "Algo.h"

#include <iostream>
#include <cstring>
#include <bits/stdc++.h>

using namespace std;

void displayOutput(list<Node> solution, int expandedNodes, double timeTaken);

int main() {

	int puzzle[9];
	//For the user to input an initial puzzle problem
	cout << "Enter your puzzle : \n";
	for(int i = 0; i < 9; i++) 
		cin >> puzzle[i];
	
	cout << "\nEntered puzzle : \n";
	for(int i = 0, k = 0; i < 3; i++) {

		for(int j = 0; j < 3; j++) {
			cout << puzzle[k] << " ";
			k++;
		}
		cout << "\n";
	}

	Node *root = new Node(puzzle);

	Search *aStar = new Search();
	Search *Ids = new Search();

	clock_t start, end;
	int expandedNodes;
	double timeTaken;
	list<Node> solution;

/* Displaying output for A* Search */
		start = clock();
	solution = aStar->AStarSearch(*root);
	expandedNodes = aStar->expandedNodes;
		end = clock();
	timeTaken = double(end - start) / double(CLOCKS_PER_SEC);
	
	cout << "\n\n-----------A* Algorithm (Manhattan Distance heuristics)-----------" << endl;
	displayOutput(solution, expandedNodes, timeTaken);

/* Displaying output for Iterative Deepening Search */
		start = clock();
	solution = Ids->IterativeDeepeningSearch(*root);
	expandedNodes = Ids->expandedNodes;
		end = clock();
	timeTaken = double(end - start) / double(CLOCKS_PER_SEC);
	
	cout << "\n\n-----------Iterative Deepening Search Algorithm evaluation----------- " << endl;
	displayOutput(solution, expandedNodes, timeTaken);
	
}

/* For displaying the required output, taking in list object and variables with values to print */
void displayOutput(list<Node> solution, int expandedNodes, double timeTaken) {

	if(solution.size() > 0) {
			int pathCost = -1;
			
			cout << "Path : ";
			for(list<Node>::iterator it = solution.begin(); it != solution.end(); it++) {
				cout << it->moves << "-";
				pathCost++;
			}

			cout << "\nExpanded Nodes: " << expandedNodes << endl;
			cout << "Time taken by program is : " << fixed << timeTaken << setprecision(5) << " sec " << endl;
			cout << "Solution Path Cost: " << pathCost << endl;

			cout << "\nSolution Path: ";
			for(list<Node>::iterator it = solution.begin(); it != solution.end(); it++) {
				cout << "\n" << it->moves << "-";
				it->printPuzzle();
			}
	} else 
		cout << "No path to solution. \n";
}















// int puzzle[] = {1, 2, 3,
// 				0, 6, 4,
// 				8, 7, 5};

// int puzzle1[] = {1, 3, 4,
// 				8, 6, 2,
// 				7, 0, 5};	//easy

// int puzzle2[] = {2, 8, 1,
// 				0, 4, 3,
// 				7, 6, 5};	//medium

// int puzzle3[] = {2, 8, 1,
// 				4, 6, 3,
// 				7, 5, 0};	//hard

// int puzzle4[] = {5, 6, 7,
// 				4, 0, 8,
// 				3, 2, 1};	//worst