from turtle import Turtle


SEGMENT_SIZE = 20

HEAD_UP = 90
HEAD_DOWN = 270
HEAD_RIGHT = 0
HEAD_LEFT = 180


class Snake:
    def __init__(self, starting_segments=3):
        self.snake = []
        self.difficulty = 0.5
        self.new_snake(starting_segments=3)
        self.snake_head = self.snake[0]
        self.snake_head_next_heading = self.snake_head.heading()

    def set_difficulty(self, level=1):
        # level=1 -> easy / level=2 -> medium / level=3 -> hard
        self.difficulty = 0.5 - (level-1)*0.2

    def new_snake(self, starting_segments=3):
        self.add_head()
        for _ in range(starting_segments - 1):
            self.add_segment()
        self.snake_head = self.snake[0]
        self.snake_head_next_heading = self.snake_head.heading()

    def add_head(self):
        head = Turtle()
        head.shape("square")
        head.color("yellow")
        head.penup()
        head.goto(0, 0)
        self.snake.append(head)

    def add_segment(self):
        last_segment_heading = self.snake[-1].heading()
        last_segment_position = self.snake[-1].pos()
        if last_segment_heading == HEAD_RIGHT:
            new_segment_position_x = last_segment_position[0] - SEGMENT_SIZE
            new_segment_position_y = last_segment_position[1]
        elif last_segment_heading == HEAD_UP:
            new_segment_position_x = last_segment_position[0]
            new_segment_position_y = last_segment_position[1] - SEGMENT_SIZE
        elif last_segment_heading == HEAD_LEFT:
            new_segment_position_x = last_segment_position[0] + SEGMENT_SIZE
            new_segment_position_y = last_segment_position[1]
        else:
            new_segment_position_x = last_segment_position[0]
            new_segment_position_y = last_segment_position[1] + SEGMENT_SIZE
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(new_segment_position_x, new_segment_position_y)
        new_segment.setheading(last_segment_heading)
        self.snake.append(new_segment)

    def move_snake_up(self):
        if self.snake_head.heading() != HEAD_DOWN:
            self.snake_head_next_heading = HEAD_UP

    def move_snake_down(self):
        if self.snake_head.heading() != HEAD_UP:
            self.snake_head_next_heading = HEAD_DOWN

    def move_snake_right(self):
        if self.snake_head.heading() != HEAD_LEFT:
            self.snake_head_next_heading = HEAD_RIGHT

    def move_snake_left(self):
        if self.snake_head.heading() != HEAD_RIGHT:
            self.snake_head_next_heading = HEAD_LEFT

    def move_snake(self):
        next_segment_heading = self.snake_head_next_heading
        for segment in self.snake:
            current_segment_heading = segment.heading()
            segment.setheading(next_segment_heading)
            segment.forward(SEGMENT_SIZE)
            next_segment_heading = current_segment_heading

    def reset_snake(self):
        for segment in self.snake:
            segment.hideturtle()
            del segment
        self.snake.clear()


