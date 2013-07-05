#include <stdio.h>
#include <string.h>

int main() {

	char line[10000];
	char line2[10000];
	long songCount;
	long songToBeSelected;
	int ctr;
	int ctr2;
	int selectedSongs = 0;
	int highest = 0;
	int highest2 = 0;
	int lastHighest = 0;
	int isFirst = 1;
	int reseted = 0;

	scanf("%s %s", line, line2);

	songCount = atol(line);
	songToBeSelected = atol(line2);

	int songQuality[songCount];
	char songName[songCount][10000];

	for(ctr = 0; ctr < songCount; ctr++) {
		scanf("%s %s", line, line2);
		songQuality[ctr] = atol(line) * (ctr + 1);
		//songName[ctr] = line2;
		strcpy(songName[ctr], line2);
	}

	
	while(selectedSongs != songToBeSelected) {

		for(ctr=0;ctr < songCount; ctr++) {

			if(isFirst == 1) {

				if(songQuality[ctr] > highest) {
					highest = songQuality[ctr];
					//lastHighest = highest;
				}

			} else {
				if(songQuality[ctr] < lastHighest) {

					if(reseted == 1) {
						highest = 0;
						reseted = 0;
					}

					if(songQuality[ctr] > highest) {
						highest = songQuality[ctr];
						//lastHighest = highest;
					}					

				}
			}

		}

		lastHighest = highest;
		isFirst = 0;
		reseted = 1;


		for(ctr = 0; ctr < songCount; ctr ++) {

			if(songQuality[ctr] == highest) {
				printf("%s\n", songName[ctr]);
				selectedSongs = selectedSongs + 1;
			}

		}


	}
	

	return 0;

}