#include <iostream>
#include <string>
#include <fstream>

#include "Console.h"
#include "Game.h"

using namespace std;
typedef unsigned int uint;

static const string hs_file = "hs.bin";

void getHighScore(uint& highscore) {
	ifstream in(hs_file, ios_base::binary);

	if (!in)
		return;

	in.read((char*)&highscore, sizeof(highscore));
	if (!in.good())
		highscore = 0;

	in.close();
}

void setHighScore(uint& highscore) {
	ofstream out(hs_file, ios_base::binary);

	if (!out)
		return;

	out.write((char*)&highscore, sizeof(highscore));
	out.close();
}

void startTheGame() {
	setConsoleColour(FOREGROUND_GREEN | FOREGROUND_INTENSITY);
	Game snake(25, 60, 4);

	uint score = 0;
	uint highscore = 0;
	getHighScore(highscore);

	while (true) {
		bool collision = !snake.update();
		score = snake.getScore();

		if (score > highscore) {
			highscore = score;
			setHighScore(highscore);
		}

		snake.draw();
		
		cout << endl << "Score: " << setw(3) << score << "\tHighscore: " << setw(3) << highscore << endl;

		if (collision)
			break;

		_sleep(75);
	}
}


int main() {
	char restart;

	do {
		startTheGame();

		cout << "Do you want to play again (Y/N): "; 
		cin >> restart;
		restart = tolower(restart);
		cin.ignore();
	} 
	while (restart == 'y');

	return 0;
}