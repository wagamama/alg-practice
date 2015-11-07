#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

class HashTable
{
public:
    HashTable()
    {
        size = 11;
        slot = vector<int>(size, -1);
        data = vector<string>(size, "");
    }

    ~HashTable()
    {
    }

    void put(int key, string data);
    string get(int key);

public:
    vector<int> slot;
    vector<string> data;

private:
    int hashfunction(int key);
    int rehash(int oldhash);

private:
    int size;
};

int HashTable::hashfunction(int key)
{
    return key % size;
}

int HashTable::rehash(int oldhash)
{
    return (oldhash+1) % size;
}

void HashTable::put(int key, string value)
{
    int hashvalue = hashfunction(key);

    if (slot[hashvalue] == -1)
    {
        slot[hashvalue] = key;
        data[hashvalue] = value;
    }
    else
    {
        if (slot[hashvalue] == key)
        {
            data[hashvalue] = value;
        }
        else
        {
            int nextslot = rehash(hashvalue);
            while (slot[nextslot] != -1 && slot[nextslot] != key)
            {
                nextslot = rehash(nextslot);
            }

            if (slot[nextslot] == -1)
            {
                slot[nextslot] = key;
                data[nextslot] = value;
            }
            else
            {
                data[nextslot] = value;
            }
        }
    }
}

string HashTable::get(int key)
{
    int startslot = hashfunction(key);

    string value = "";
    bool stop = false;
    bool found = false;
    int position = startslot;

    while (slot[position] != -1 && !stop && !found)
    {
        if (slot[position] == key)
        {
            found = true;
            value = data[position];
        }
        else
        {
            position = rehash(position);
            if (position == startslot)
            {
                stop = true;
            }
        }
    }

    return value;
}

int main(void)
{
    HashTable h = HashTable();
    h.put(54, "cat");
    h.put(26, "dot");
    h.put(93, "lion");
    h.put(17, "tiger");
    h.put(77, "bird");
    h.put(31, "cow");
    h.put(44, "goat");
    h.put(55, "pig");
    h.put(20, "chicken");
    for (int i = 0; i < h.slot.size(); i++)
    {
        printf("%d ", h.slot[i]);
    }
    printf("\n");
    for (int i = 0; i < h.data.size(); i++)
    {
        std::string data = h.data[i];
        if (data == "")
            data = "''";
        printf("%s ", data.c_str());
    }
    printf("\n");
    printf("%s\n", h.get(20).c_str());
    printf("%s\n", h.get(17).c_str());
    h.put(20, "duck");
    printf("%s\n", h.get(20).c_str());

    return 0;
}
