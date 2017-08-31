from flask import Flask, redirect, render_template, request, url_for
from server import app

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        list_input = request.form["list_input"]
        
        return redirect(url_for("hello", list_input=list_input))
 
    return render_template("index.html")

@app.route("/hello",methods=["GET", "POST"])
def hello():
    list_input = request.args['list_input']
    print("HELlo")
    input_list = [int(x) for x in list_input.split(',')]
    bigList = []
    swapped = 1
    while swapped == 1:
        for index in range(0, len(input_list)-1):
            swapped = 0
            if input_list[index] > input_list[index+1]:
                input_list[index], input_list[index+1] = input_list[index+1], input_list[index]
                swapped = 1
                bigList.append(list(input_list))
                break

    return render_template("hello.html", input_list = bigList)
