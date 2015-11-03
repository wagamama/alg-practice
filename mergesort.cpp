#include "stdio.h"
#include "cstring"

void mergesort(int* list, int len)
{
    if (len == 1)
        return;

    int mid = len / 2;
    int rest = len - mid;
    int left[mid];
    std::memcpy(left, &list[0], mid*sizeof(int));
    int right[rest];
    std::memcpy(right, &list[mid], rest*sizeof(int));

    mergesort(left, mid);
    mergesort(right, rest);

    int i = 0;
    int j = 0;
    int k = 0;
    while (i < mid && j < rest)
    {
        if (left[i] < right[j])
        {
            list[k] = left[i];
            i++;
        }
        else
        {
            list[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < mid)
    {
        list[k] = left[i];
        i++;
        k++;
    }

    while (j < rest)
    {
        list[k] = right[j];
        j++;
        k++;
    }
}

int main(void)
{
    int list[] = {54,26,93,17,77,31,44,55,20};
    mergesort(list, 9);
    for (int i = 0; i < 9; i++)
    {
        printf("%d ", list[i]);
    }
    printf("\n");

    return 0;
}
