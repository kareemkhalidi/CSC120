My creative program is a small simulation that only implements one class. Every 30 frames, a new consumer obj is created.
The consumer obj is a circle that moves diagonally around and bounces off the walls. The consumer spawner gives each
consumer a random position, a random size from 10 to 50, a random speed from 1 to 5, and a random verticle and horizontal
direction to travel. The consumer obj will bounce around until it contacts another consumer. When two consumers contact, the
one with a larger radius "consumes" the smaller one. Basically the smaller obj is removed and its radius is added to the larger one.
Once a consumer reaches a radius of 400 or greater, it is removed and the score is increased by one. In order to do this I had to
modify the three_shapes_game.py program and add the method do_score_calls. In order to run this program, just hit the run button.
After that it is just a simulation.