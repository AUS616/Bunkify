from flask import Flask, render_template, request, url_for
import math

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    attendance_percentage = None
    status = None
    selected_attendance = 75
    bunkable_classes = None
    attend_classes = None
    if request.method == 'POST':
        try:
            total_classes = int(request.form['total_classes'])
            classes_attended = int(request.form['classes_attended'])
            min_percentage = int(request.form['min_percentage'])
            selected_percentage = min_percentage
            attendance_percentage = (classes_attended / total_classes) * 100
            max_allowed_classes = total_classes - (total_classes * (min_percentage/100))
            classes_missed = total_classes - classes_attended
            bunkable_classes = math.ceil(max_allowed_classes - classes_missed)
            attend_classes = math.ceil(total_classes * (min_percentage/100))
            
            if attendance_percentage >= min_percentage:
                status = "You are eligible to sit for the exam."
                

            else:
                status = "You are not eligible to sit for the exam."
                bunkable_classes = None



        except:
            status = "Please enter valid numbers for total classes and classes attended."
            attendance_percentage = None
    return render_template('index.html', attendance_percentage=attendance_percentage, status=status, selected_attendance=selected_attendance,bunkable_classes=bunkable_classes,attend_classes=attend_classes)


if __name__ == "__main__":
    app.run()
