import cs50
import csv
import numpy

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    selfless = request.form.get("selfless")
    religion = request.form.get("religion")
    god = request.form.get("god")
    politics = request.form.get("politics")
    celebrities = request.form.get("celebrities")
    culture = request.form.get("culture")
    thinking = request.form.get("thinking")
    shock = request.form.get("shock")
    moral = request.form.get("lesson")
    parody = request.form.get("parody")

    #if not others or not religion or not God or not politics or not celebrities or not culture or not thinking or not shock or not lesson or not parody:
    #    return render_template("error.html", message="get it together!")
    reader = csv.reader(open("ratings.csv", "r"), delimiter=",")
    x = list(reader)


    #Create Matrix of Episode vectors
    global episode_matrix
    episode_matrix = numpy.array(x).astype("float")
    #print(episode_matrix)

    #Make user vector
    y = [selfless, religion, god, politics, celebrities, culture, thinking, shock, moral, parody]

    for category in y:
        if category != -10 and category != -9 and category != -8 and category != -7 and category != -6  and category != -5  and category != -4  and category != -3  and category != -2  and category != -1  and category != 0  and category != 1  and category != 2  and category != 3  and category != 4  and category != 5 and category != 6 and category != 7  and category != 8 and category != 9 and category != 10:
            category = 0

    human = numpy.array(y).astype("int")

    #Empty Matrices
    shape = (34,10)
    difference = numpy.empty(shape)
    column = (34,1)
    magnitude = numpy.empty(column)

    #Probably should count the rows instead...
    for i in range(34):
        difference[i] = human - episode_matrix[i]
        magnitude[i] = numpy.linalg.norm(difference[i])




    #Make Episode List from CSV

    reader = csv.reader(open("episodes.csv", "r"), delimiter=",")
    episode_list = list(reader)

    #check if list loads correctly
    #print(episode_list)

    #Return Episode Title
    index_min = numpy.argmin(magnitude)
    global row
    row = index_min

    print("row:", row)


    print("you need to watch:", episode_list[row])

    perfect_episode = ''.join(episode_list[row])

    #perfect_episode = perfect_episode.join

 #   accurate = "dummyvar"
 #   accurate = input("Did the episode fit like a glove - y or n?" )
 #   attribute = 100.0
 #   if accurate == "n" or accurate == "N":
  #      while attribute > 10.0:
     #       attribute = cs50.get_int("How did the episode let you down?: General Angst(0), Religion(1), God(2), Politics(3), Celebrities(4), Culture(5), Thought (6), Shock(7), Moral Lesson (8), Parody(9)?")

    #    change = input("Too much(M) or too little(L)?")
   #     if change == "M" or change == "m":
    #        episode_matrix[row][attribute] -= 1
    #    if change == "L" or change == "l":
#            episode_matrix[row][attribute] += 1

        #rewrite ratings file SOMEHOW
   #     numpy.savetxt("ratings.csv", episode_matrix, delimiter=",")


    #with open("survey.csv", "a", newline="") as file:
    #    columns = ["others", "others", "others"]
    #    writer = csv.DictWriter(file, fieldnames=columns)
    #    writer.writerow({"others": others, "others": others, "others": others})
    #return redirect("/sheet.html", code=302)
    return render_template("sheet.html", variable = perfect_episode)

    #if __name__ == '__main__':
    #app.run()


@app.route("/sheet", methods=["POST"])
def post_sheet():


#semen = True
#while semen == True:
    if request.form.get("fit") == "not goo":

        change = request.form.get("change")
        difference = request.form.get("difference")
        print("change =", change)

        if change == "Other People":
            change = 0
        elif change == "Religion":
            change = 1
        elif change == "God":
            change = 2
        elif change == "Politics":
            change = 3
        elif change == "Celebrities":
            change = 4
        elif change == "Culture":
            change = 5
        elif change == "Thinking":
            change = 6
        elif change == "Shock":
            change = 7
        elif change == "Lesson":
            change = 8
        elif change == "Parody":
            change = 9


        print("change =", change)



        if difference == "Too much":
            episode_matrix[row][change] += 1
            print("change =", change)
        if difference == "Too little":
            episode_matrix[row][change] -= 1
            print("change =", change)

        #rewrite ratings file SOMEHOW
        numpy.savetxt("ratings.csv", episode_matrix, delimiter=",")
        return render_template("thankyou.html")

    elif request.form.get("fit") == "vewygoo":
        return render_template("thankyou.html")


