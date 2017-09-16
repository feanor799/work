#ifndef SNAKE_H
#define SNAKE_H

#include "Grid.h"

typedef vector<Point> snake_t;

enum DIRECTION {
	UP,
	DOWN,
	LEFT,
	RIGHT
};

class Snake {
public:
	Snake();
	Snake(Grid &grid, int start_size, DIRECTION start_direction);

	bool move();
	void grow();
	void setDirection(DIRECTION direction);

	bool isSnake(Point &p);

	snake_t getSnake();
	Grid getGrid();

private:
	snake_t snake_;
	Grid grid_;
	DIRECTION direction_;
};

#endif // !SNAKE_H
