#include <iostream>

using namespace std;

// Function Inputs:
// n: number of coins
// char coins[] : coins represented using a character array containing only H (Heads) and T (Tails)
// int flips[] : stores the index of removed coin (assuming that Coins are numbered starting from 1 in the removal sequence although array indices start from 0)
// int count : the number of coins removed

// Function Outputs:
// a boolean possible: to tell if it is possible to remove all coins
// given that: A coin can only be removed if it currently shows Heads (H).
// and when a coin is removed, only its immediate original neighbors are flipped, provided they have not already been removed.

bool removeCoins(int n, char coins[], int flips[], int &count) {

    bool removed[100] = {false};
    int remaining = n;
    count = 0;

    // Loop on the remaining coins
    while (remaining > 0) {

        int i = 0;

        // Find the first Heads coin from the left (greedy)
        while (i < n && (removed[i] || coins[i] != 'H')) {
            i++;
        }

        // No Heads coin found
        if (i == n) {
            return false;
        }

        // Remove Heads coin
        removed[i] = true;
        remaining--;

        flips[count] = i + 1;
        count++;

        // Flip its left neighbor
        if (i > 0 && !removed[i - 1]) {
            if (coins[i - 1] == 'H')
                coins[i - 1] = 'T';
            else
                coins[i - 1] = 'H';
        }

        // Flip its right neighbor
        if (i < n - 1 && !removed[i + 1]) {
            if (coins[i + 1] == 'H')
                coins[i + 1] = 'T';
            else
                coins[i + 1] = 'H';
        }
    }

    return true;
}

int main() {

    // takes the number of coins and their state whether they are H or T as input from user

    int n;
    cin >> n;

    char coins[100];
    int flips[100];
    int count;

    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    // calls algorithm function
    bool possible = removeCoins(n, coins, flips, count);

    // outputs boolean and flips array
    if (possible) {
        cout << "Possible\n";

        cout << "Removal sequence: ";

        for (int i = 0; i < count; i++) {
            cout << flips[i] << " ";
        }
    }
    else {
        cout << "Not Possible";
    }

    return 0;
}

// Time complexity: O(n^2)
// Space complexity: O(n)
