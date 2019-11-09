/*
 For Spotify Summer 2013 Internship position
 Zipf's Songs (Problem ID: zipfsong)
 Imankalyan Mukherjee
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main (int argc, char * const argv[]) {
    
	string STRING;
    string INPUT;
    
    printf("Started \n");
    
	// Read the Input from stdin
    
	// Read the number of songs in the album
	getline(cin,STRING,' ');
	int num = atoi(STRING.c_str());
	
	// Read the number of songs to list
	getline(cin,STRING,'\n');
	int req = atoi(STRING.c_str());
	
	int count[num];
    vector<string> name(num);
    
	float quality[num];
	int chart[req];
	
	int i = 0;
	
	// Read the remaining file for the enlisting 1) Listen count 2) Name
	while(i < num)
	{
		// Read the listen count
		getline(cin,STRING,' ');
		count[i] = atoi(STRING.c_str());
		
		// Read the name
		getline(cin,STRING,'\n');
		name.at(i) = STRING;
		
		i++;
	}
	
	// Calculate quality of each
	for(i = 0; i < num; i++)
	{
		quality[i] = count[i]/(num - i);
	}
	
	float maximum = 0.0;
	int top = 0;
	int j = 0;
	
	// Sort as per quality
	for(i = 0; i < req; i++)
	{
		for (j = 0; j < num; j++)
		{
			if (quality[j] > maximum)
			{
				maximum = quality[j];
				chart[i]  = j;
			}
		}
		
		// Re-initialize to find the next highest
		top = chart[i];
		quality[top] = 0.0;
		maximum = 0.0;
		
		// Print the topmost track name
		cout<<endl<<name[top]<<endl;
	}
	
    return 0;
    
}
