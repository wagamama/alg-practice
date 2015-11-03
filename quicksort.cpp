#include "stdio.h"

int partition(int* list, int first, int last)
{
    int pivotValue = list[first];
    int left = first + 1;
    int right = last;

    bool done = false;
    while (!done)
    {
        while (left <= right && list[left] <= pivotValue)
            left++;
        while (left <= right && list[right] >= pivotValue)
            right--;

        if (right < left)
            done = true;
        else
        {
            int tmp = list[left];
            list[left] = list[right];
            list[right] = tmp;
        }
    }

    int tmp = list[right];
    list[right] = list[first];
    list[first] = tmp;

    return right;
}

void quicksort(int* list, int first, int last)
{
    if (first < last)
    {
        int split = partition(list, first, last);
        quicksort(list, first, split-1);
        quicksort(list, split+1, last);
    }
}

int main(void)
{
    int list[] = {54, 26, 93, 17, 77, 31, 44, 55, 20};
    quicksort(list, 0, 8);
    for (int i = 0; i < 9; i++)
    {
        printf("%d ", list[i]);
    }
    printf("\n");

    return 0;
}
