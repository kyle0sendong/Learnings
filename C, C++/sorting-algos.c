/* 
  Group of : Kyle Destura
             Gabriel Jacob Guianan
             Roanne Pearl Misolas
  BSCS 2-B
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertionSort(int array[], int N);

void mergeSort(int array[], int start, int end);
void merge(int array[], int start, int mid, int end);

void quickSort(int array[], int start, int end);
int partition (int array[], int start, int end);
int medianOfThree(int array[], int low, int high);

void heapSort(int array[], int n);
void heapify(int array[], int n, int i);

void swap(int* a, int* b);

int main() {

    clock_t start, end;
    double cpu_time_used;

    FILE *outputPtr;
    outputPtr = fopen("output.txt", "w");

    printf("This program outputs the computation time of a 4 sorting algorithm.\n");
    printf("1. Insertion Sort    2. Merge Sort    3. Quick Sort    4.Heap Sort\n\n");


    char term;  //for ignoring non integer characters after the input 
    int N;
    printf("Enter the input size for the array to be used: ");
    scanf("%d%c", &N, &term);

    while(N < 2 ) { //error checking if input size is less than 2
          N = 0;
          term = '\0';
          printf("Enter only integer above 1: ");
          scanf("%d%c", &N, &term);
    }

    int array1[N];

    char choice[10];
    printf("Enter [1] for unsorted array.\n");
    printf("Enter [2] for sorted array.\n");
    scanf("%s", &choice);

    while( !(choice[0] == '1' || choice[0] == '2') ) {  //check user input
      choice[0] = '\0'; //empty the string
      printf("Please enter only [1] or [2]: ");
      scanf("%s", &choice);
    }

    if (choice[0] == '1') { //Choice 1 is for getting the computation

        //declare 3 more copies of array 1 for each sorting algorithm.
        int array2[N];
        int array3[N];
        int array4[N];

        printf("Generating %d Random Integers . . .\n", N);
        fprintf(outputPtr, "Randomly Generated Array with size %d:\n", N);

        const int MAXRANGE = 1000000; 
        srand(time(0));
        for(int i = 0; i < N; i++) {
            array1[i] = (rand() % (MAXRANGE - 0 + 1) + 0);
            array2[i] = array1[i];  //duplicates of array1 for similar cases
            array3[i] = array1[i];
            array4[i] = array1[i];
            fprintf(outputPtr, "%d ", array1[i]);
        }
        
        printf("Calculating time taken to sort . . .\n\n");
        fprintf(outputPtr, "\n\nComputation Time T(N): \n");

        //insertion sort time
        start = clock();
          insertionSort(array1, N);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Insertion Sort: %lf s\n", cpu_time_used);
        fprintf(outputPtr, "\nComputation Time of Insertion Sort: %lf s\n", cpu_time_used);

        //merge sort time
        start = clock();
          mergeSort(array2, 0, N-1); end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Merge Sort:     %lf s\n", cpu_time_used);
        fprintf(outputPtr, "Computation Time of Merge Sort:     %lf s\n", cpu_time_used);

        //quick sort time
        start = clock();
          quickSort(array3, 0, N-1);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Quick Sort:     %lf s\n", cpu_time_used);
        fprintf(outputPtr, "Computation Time of Quick Sort:     %lf s\n", cpu_time_used);

        //heap sort time
        start = clock();
          heapSort(array4, N);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Heap Sort:      %lf s\n", cpu_time_used);
        fprintf(outputPtr, "Computation Time of Heap Sort:      %lf s\n", cpu_time_used);

    } else if (choice[0] == '2') {

        int X;  //variable storage for any positive integer user input
        printf("\nPlease enter any positive integer: ");
        scanf("%d%c", &X, &term);

        while(X < 1 ) { //error checking if X is not a positive integer
          X = 0;
          term = '\0';
          printf("Enter only positive integer: ");
          scanf("%d%c", &X, &term);
        }

        fprintf(outputPtr, "Original Array: with size %d\n", N);
        printf("\nGenerating %d integers in an increasing order . . .\n", N);
        for(int i = 0; i < N; i++) {  //filling up the array with an increasing order ( N + (i+1)X ) every iteration
            array1[i] = N + ((i+1) * X);
            fprintf(outputPtr, "%d ", array1[i]);
        }

        printf("\nCalculating time taken to sort . . .\n\n");
        fprintf(outputPtr, "\n\nComputation Time T(N): \n");

        //insertion sort time
        start = clock();
          insertionSort(array1, N);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Insertion Sort: %lf s\n", cpu_time_used);
        fprintf(outputPtr, "\nComputation Time of Insertion Sort: %lf s\n", cpu_time_used);

        //merge sort time
        start = clock();
          mergeSort(array1, 0, N-1);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Merge Sort:     %lf s\n", cpu_time_used);
        fprintf(outputPtr, "Computation Time of Merge Sort:     %lf s\n", cpu_time_used);

        //quick sort time
        start = clock();
          quickSort(array1, 0, N-1);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Quick Sort:     %lf s\n", cpu_time_used);
        fprintf(outputPtr, "Computation Time of Quick Sort:     %lf s\n", cpu_time_used);

        //heap sort computation time 
        start = clock();
          heapSort(array1, N);
        end = clock();
        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("Computation Time of Heap Sort:      %lf s\n", cpu_time_used);
        fprintf(outputPtr, "Computation Time of Heap Sort:      %lf s\n", cpu_time_used);

    }

    //outputs the sorted array file
    fprintf(outputPtr, "\nSorted Array: \n");
    for(int i = 0; i < N; i++)
        fprintf(outputPtr, "%d ", array1[i]);
    fprintf(outputPtr, "\n\n");

    fclose(outputPtr);  //close the file pointer
    return 0;
}


//Function definitions. . . .
//these are generic sorting algorithms
//only difference is the quick sort and its pivot selecting method
//insertion sort
void insertionSort(int array[], int N) {

  for (int i = 1; i < N; i++) {
    int key = array[i];
    int j = i - 1;

    while (key < array[j] && j >= 0) {
      array[j + 1] = array[j];
      j--;
    }
    array[j + 1] = key;
  }
}

//merge sort
void mergeSort(int array[], int start, int end) {

	if(start < end) {
		int mid = (start + end) / 2;
		mergeSort(array, start, mid);
		mergeSort(array, mid+1, end);
		merge(array, start, mid, end);
	}
}
void merge(int array[], int start, int mid, int end) {

	int tempArray[end - start + 1];
	int i = start;
	int j = mid + 1;
	int k = 0;

	// traverse both arrays and in each iteration add smaller of both elements in temp
	while(i <= mid && j <= end) {
		if(array[i] <= array[j]) {
			tempArray[k] = array[i];
			k += 1; i += 1;
		}
		else {
			tempArray[k] = array[j];
			k += 1; j += 1;
		}
	}

	// add elements left in the first interval
	while(i <= mid) {
		tempArray[k] = array[i];
		k += 1; i += 1;
	}

	// add elements left in the second interval
	while(j <= end) {
		tempArray[k] = array[j];
		k += 1; j += 1;
	}

	// copy temp to original interval
	for(i = start; i <= end; i += 1) {
		array[i] = tempArray[i - start];
	}
}

//quick sort
void quickSort(int array[], int low, int high) {
    while (low < high) {
        int j = partition(array, low, high);
        if (j - low < high -j) {
            quickSort(array, low, j-1);
            low = j+1;
        } else {
            quickSort(array, j+1, high);
            high = j-1;
        }
    }
}
int partition(int array[], int low, int high) {

  int pivot = medianOfThree(array, low, high);  //instead of using the left most or right most, median of 3 is used

  // pointer for greater element
  int i = (low - 1);

  for (int j = low; j < high; j++) {

    if (array[j] <= pivot) {
      i++;
      swap(array + i, array + j);
    }
  }

  // swap the pivot element with the greater element at i
  swap(array + (i + 1), array + high);

  // return the partition point
  return (i + 1);
}

//function for taking median of three, specific use only for the quick sort
int medianOfThree(int array[], int low, int high) {
  int v0 = array[low];
  int v1 = array[ (high - low) / 2 + 1];
  int v2 = array[high];

//source code from https://stackoverflow.com/questions/7559608/median-of-three-values-strategy 
// This uses XOR like operator. So you would read:
// Is a greater than exclusively one of the others? return a
// Is b greater than exclusively one of the others? return b
// If none of above: return c
  if ((v0 > v1) ^ (v0 > v2)) 
        return v0;
    else if ((v2 < v0) ^ (v1 < v2)) 
        return v1;
    else
        return v2;
}

//heap sort
void heapSort(int arr[], int size) {

    for (int i = size / 2 - 1; i >= 0; i--)
        heapify(arr, size, i);

    for (int i=size-1; i>=0; i--) {
        swap(arr + 0, arr + i);
        heapify(arr, i, 0);
    }

}
void heapify(int arr[], int size, int i) {  //max heap is implemented
    int largest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;
    int temp;

    if (left < size && arr[left] >arr[largest])
        largest = left;

    if (right < size && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr + i, arr + largest);
        heapify(arr, size, largest);
    }
}


void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}