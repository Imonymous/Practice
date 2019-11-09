//============================================================================
// Name        : TEST.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

bool myComparator(pair<float, int> p1, pair<float, int> p2) {
	return p1.first > p2.first;
}

int main(int argc, char * const argv[]) {

	int n, m;

	// Read the Input n and m from stdin
	scanf("%d%d", &n, &m);

	// To store given frequencies
	int freq[n];

	// To store n song names each with max 30 characters, as mentioned in the puzzle
	char names[n][30];

	int totalSongs = 0;
	float totalDividends = 0;

	// Read the remaining file for the enlisting 1) Listen count 2) Name
	for (int i = 0; i < n; i++) {
		// Read the listen count
		scanf("%d", &freq[i]);

		// Read the name
		scanf("%s", names[i]);

		totalSongs += freq[i];
		totalDividends += 1.0 / (i+1);
	}

	float commonFactor = totalSongs / totalDividends;

	// To store quality of a songs along with their indices
	vector<pair<float, int> > qualityScores;

	for (int i = 0; i < n; i++) {
		// Compute frequency as per Zipf's Law which says frequency of i^th
		// element should be proportional to 1/i.
		float zipfFreq = commonFactor / (i+1);

		// Compute quality as per given formula qi = fi / zi;
		float quality = freq[i] / zipfFreq;

		// Create a pair of quality and corresponding song index
		pair<float, int> p(quality, i);

		// Add into vector
		qualityScores.push_back(p);
	}


	// stable_sort sorts all elements of quality vector as per their quality.
	// stable_sort should be used instead of simple sort, because we want to
	//       display first name in the list in case multiple names have same
	//       quality. stable_sort maintains relative order while sorting.
	// myComparator is a function to sort elements in decreasing order of
	//       qualities.
	stable_sort(qualityScores.begin(), qualityScores.end(), myComparator);

	// Initialize 'it' with first element of vector quality
	vector<pair<float, int> >::iterator it = qualityScores.begin();

	// Print first m best songs
	for (int i = 0; i < m; i++, it++) {
		// Read index of the song at current position
		int index = (*it).second;

		// Print name of song at index
		cout << names[index] << endl;
	}
	return 0;
}
