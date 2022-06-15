import model

def main():
    mod = model.Model("Candy Kitty")

    # set win condition
    mod.set_prop("win_condition", 100)
    mod.set_prop("lose_condition", 0)

    candy_id = mod.add_entity("Candy")
    candy = mod.get_entity(candy_id)
    mod.add_comp(model.components.Body2D(mod.gen_id("B2D"), (5, 5), (1, 1)), candy)
    mod.add_comp(model.components.Sprite(mod.gen_id("SPR"), [], (0,0)), candy)
    mod.add_comp(model.components.Camera(mod.gen_id("CAM"), (720, 1440), (0, 0)), candy)

    candy.set_prop("hp", 100)
    candy.set_prop("score", 0)
    candy.add_tag("player")

    snake_id = mod.add_entity("Snake")
    snake = mod.get_entity(snake_id)
    mod.add_comp(model.components.Body2D(mod.gen_id("B2D"), (5, 5), (1, 1)), snake)
    mod.add_comp(model.components.Sprite(mod.gen_id("SPR"), [], (0,0)), snake)

    snake.set_prop("hp", 100)
    snake.set_prop("dmg", 0)
    snake.add_tag("enemy")


    print(mod.peek())

if __name__ == "__main__":
    main()
