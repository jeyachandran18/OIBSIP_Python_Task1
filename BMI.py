import turtle as t

# Create screen and turtle
screen = t.Screen()
screen.title("BMI Calculator using Turtle")
pen = t.Turtle()
pen.hideturtle()
pen.penup()

# Ask user for inputs (in popup dialogs)
weight = screen.numinput("Weight", "Enter your weight in kg:", minval=1, maxval=500)
height = screen.numinput("Height", "Enter your height in meters (e.g. 1.75):", minval=0.5, maxval=2.5)

# Calculate BMI
bmi = weight / (height ** 2)

# Determine category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display result
pen.goto(0, 40)
pen.write(f"Weight: {weight} kg", align="center", font=("Arial", 16, "normal"))

pen.goto(0, 10)
pen.write(f"Height: {height} m", align="center", font=("Arial", 16, "normal"))

pen.goto(0, -20)
pen.write(f"BMI: {bmi:.2f}", align="center", font=("Arial", 18, "bold"))

pen.goto(0, -50)
pen.write(f"Category: {category}", align="center", font=("Arial", 18, "normal"))

# Wait for click to close
screen.exitonclick()
