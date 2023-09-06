import turtle
import pandas

screen = turtle.Screen()
screen.title("Asian Countries Quiz")
image = "asia_map.gif"
screen.addshape(image)
turtle.shape(image)

# x_cor = []
# y_cor = []
#
#
# def get_mouseclick_cor(x, y):
#     x_cor.append(int(x))
#     y_cor.append(int(y))
#     if len(x_cor) == 50 and len(y_cor) == 50:
#         print(x_cor)
#         print(y_cor)
#
#
# screen.onscreenclick(get_mouseclick_cor)
# turtle.mainloop()

# x_cor = [-144, -208, -190, -209, -66, -62, 23, -12, -9, -263, -199, -107, 36, -190, -224, -260, 118, -254, -122, -216, -104, -22, -250, -20, -137, -4, -43, -87, 74, -188, -136, -257, 56, -208, 0, -238, -15, 79, -106, -239, 50, -124, -24, 67, -247, -162, -199, -145, 2, -227]
# y_cor = [18, 45, 56, -13, -26, -10, -107, -73, 8, 23, 60, -28, -136, 11, 13, 8, 29, 6, 73, -1, 52, -41, 23, -106, -120, 71, -35, -6, 44, -39, 2, 14, -78, -17, 144, -17, -121, 29, -97, 23, -26, 39, -57, -166, 46, 42, -27, 54, -61, -63]
#
# df = pandas.read_csv("countries_in_asia.csv")
# df["x"] = x_cor
# df["y"] = y_cor
# df.to_csv("countries_with_cor.csv")

data = pandas.read_csv("countries_with_cor.csv")
all_countries = list(data.countries)
guessed_countries = []

while len(guessed_countries) < 50:
    answer = screen.textinput(title=f"{len(guessed_countries)}/50 Correct", prompt="Guess a Country in Asia").title()
    if answer == "Exit":
        countries_to_learn = list(set(all_countries) - set(guessed_countries))
        con_dict = {
            "to_learn": countries_to_learn
        }
        df = pandas.DataFrame(con_dict)
        df.to_csv("countries_to_learn.csv")
        break
    if answer in all_countries:
        guessed_countries.append(answer)
        name_t = turtle.Turtle()
        name_t.hideturtle()
        name_t.penup()
        country_row = data[data.countries == answer]
        name_t.goto(int(country_row.x), int(country_row.y))
        name_t.write(answer)
