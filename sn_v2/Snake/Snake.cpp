#include "Snake.h"

Snake::Snake()
{
}

Snake::Snake(Grid & grid, int start_size, DIRECTION start_direction)
{
	grid_ = grid;
	direction_ = start_direction;

	snake_.push_back(grid.getCenter());

	for (int i = 0; i < start_size; i++)
		grow();
}

bool Snake::move()
{
	for (int i = snake_.size() - 1; i > 0; i--)
		snake_[i] = snake_[i - 1];

	Point &head = snake_.front();
	switch (direction_) {
		case UP:
			head.row--;
			break;

		case DOWN:
			head.row++;
			break;

		case LEFT:
			head.column--;
			break;

		case RIGHT:
			head.column++;
			break;
	}

	return !isSnake(head) && !grid_.isBorder(head);
}

void Snake::grow()
{
	Point &tail = snake_.back();
	snake_.push_back(tail);
}

void Snake::setDirection(DIRECTION direction)
{
	if ((direction_ == UP && direction == DOWN) || (direction_ == DOWN && direction == UP))
		return;

	if ((direction_ == LEFT && direction == RIGHT) || (direction_ == RIGHT && direction == LEFT))
		return;

	direction_ = direction;
}

bool Snake::isSnake(Point & p)
{
	return (find(snake_.begin() + 1, snake_.end(), p) != snake_.end());
}

snake_t Snake::getSnake()
{
	snake_t snake;

	for (auto &it = snake_.begin(); it != snake_.end() - 1; ++it) 
		snake.push_back(*it);

	return snake;
}

Grid Snake::getGrid()
{
	return grid_;
}
