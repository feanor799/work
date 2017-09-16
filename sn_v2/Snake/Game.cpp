#include "Game.h"

Game::Game(int rows, int columns, int start_size)
{
	srand(static_cast<unsigned int>(time(nullptr)));

	Point start_point{ 0, 0 };
	Point end_point{ rows, columns };

	Grid grid(start_point, end_point);
	snake_ = Snake(grid, start_size, RIGHT);

	random_fruit();
	score_ = 0;
}

bool Game::update()
{
	switch (get_user_input()) {
		case 'w':
			snake_.setDirection(UP);
			break;

		case 'a':
			snake_.setDirection(LEFT);
			break;

		case 's':
			snake_.setDirection(DOWN);
			break;

		case 'd':
			snake_.setDirection(RIGHT);
			break;

		case 'k':
			exit(0);
	}

	if (!snake_.move()) {
		return false;
	}

	if (snake_.isSnake(fruit_)) {
		random_fruit();
		snake_.grow();

		score_++;
	}

	return true;
}

void Game::draw()
{
	output_buffer_.str(string());

	Point start = snake_.getGrid().getStart();
	Point end = snake_.getGrid().getEnd();

	for (int i = 1; i <= end.row - start.row; i++) {
		for (int j = 1; j <= end.column - start.column; j++) {
			Point current_point{ start.row + i, start.column + j };

			if (current_point == fruit_)
				output_buffer_ << "D";
			else if (snake_.getGrid().isBorder(current_point))
				output_buffer_ << "#";
			else if (snake_.isSnake(current_point))
				output_buffer_ << "*";
			else
				output_buffer_ << " ";
		}

		output_buffer_ << endl;
	}
	
	system("cls");
	printf(output_buffer_.str().c_str());
}

int Game::getScore()
{
	return score_;
}

char Game::get_user_input()
{
	return tolower(_kbhit() ? _getch() : 0);
}

int Game::random_number(int min, int max)
{
	return rand() % (max - min + 1) + min;
}

Point Game::random_point()
{
	Point p;

	p.row = random_number(2, snake_.getGrid().getEnd().row - 1);
	p.column = random_number(2, snake_.getGrid().getEnd().column - 1);

	return p;
}

void Game::random_fruit()
{
	do
		fruit_ = random_point();
	while
		(snake_.isSnake(fruit_));
}
