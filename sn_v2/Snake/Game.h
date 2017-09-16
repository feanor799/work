#ifndef GAME_H
#define GAME_H

#include <iostream>
#include <ctime>
#include <conio.h>
#include <sstream>
#include "Snake.h"

using namespace std;

class Game {
public:
	Game(int rows, int columns, int start_size);

	bool update();
	void draw();

	int getScore();

private:
	Snake snake_;
	Point fruit_;
	int score_;

	char get_user_input();

	int random_number(int min, int max);
	Point random_point();
	void random_fruit();

	stringstream output_buffer_;
};

#endif // !GAME_H
