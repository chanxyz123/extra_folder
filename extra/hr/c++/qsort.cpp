#include <iostream>
#include <cstdlib>
#include <fstream>
// #include <algorithm>
using namespace std;

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
void Print(int arr[])
{
    for (int i = 0; i < 10; ++i)
    {
        cout << arr[i] <<endl;
    }
    cout << "" <<endl;
}
int partition (int arr[], int low, int high)
{
    int pivot = arr[high];   
    int i = (low - 1);  
 
    for (int j = low; j <= high- 1; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;   
            swap(&arr[i], &arr[j]);
            // Print(arr);
        }
    }
    swap(&arr[i+1],&arr[high]);
    // Print(arr);
    return (i + 1);
}
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
        Print(arr);
    }
}

int main(int argc, char const *argv[])
{
    int arr[10];
    ofstream file1("Output1.txt");
    srand(time(NULL));
    for (int i = 0; i < 10; ++i)
    {
        int v =rand()%100+1;
        arr[i] = v;
        file1  << v<< "\n";
    }
    quickSort(arr,0,100);
    ofstream file("Output.txt");
    for (int i = 0; i < 10; ++i)
    {
        file  << arr[i] << "\n";
    }
    return 0;
}