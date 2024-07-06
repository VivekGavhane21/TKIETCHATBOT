from flask import Flask, render_template, request
from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot('my Bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'I am sorry, but I do not understand.',
                      'maximum_similarity_threshold': 0.90

                  }
              ]
              )

trainer = ListTrainer(bot)
convo = [

    "Hi",
    "Helloo!",
    "Hey",

    "How are you?",
    "I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Admission Enquiry.</br>2.&emsp;Department Enquiry. </br>3.&emsp;Placement Enquiry.</br>4.&emsp;Facilities Section Enquiry.</br>5.&emsp;About TKIET.</br>",

    "Great",
    "Go ahead and write the number of any query.😃✨ <br> 1.&emsp;Admission Enquiry.</br>2.&emsp;Department Enquiry. </br>3.&emsp;Placement Enquiry.</br>4.&emsp;Facilities Section Enquiry.</br>5.&emsp;About TKIET.</br>",

    "good",
    "Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Admission Enquiry.</br>2.&emsp;Department Enquiry. </br>3.&emsp;Placement Enquiry.</br>4.&emsp;Facilities Section Enquiry.</br>5.&emsp;About TKIET.</br>",

    "fine",
    "Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Admission Enquiry.</br>2.&emsp;Department Enquiry. </br>3.&emsp;Placement Enquiry.</br>4.&emsp;Facilities Section Enquiry.</br>5.&emsp;About TKIET.</br>",

    "Thank You",
    "Your Welcome 😄",

    "Thanks",
    "Your Welcome 😄",

    "Bye",
    "Thank You for visiting!..",

    "What do you do?",
    "I am made to give Information about TKIET college.",

    "What else can you do?",
    "I can help you know more about TKIET",

    "1",
    "<b>ADMISSION <br>The following are frequently searched terms related to Admission . Please select one from the options below : <br> <br> 1.1 Courses Offered <br>1.2  Information Broucher<br>1.3  First Year B.Tech<br>1.4 Admission Comittee <br></b>",
    "1.1",
    "<b>  COURSES OFFERED <br>  These are the top results: <br> <br> 1.1.1 UG Programs <br> 1.1.2 PG Programs </b>",
    "1.1.1",
    "<b> 1.1.1 UG PROGRAMS <br>The link to UG programs 👉 <a href=" 'http://tkietwarana.ac.in/admission/UG-Programs' ">Click Here</a> </b>",
    "1.1.2",
    "<b > 1.1.2 PG PROGRAMS<br>The link to PG programs👉 <a href=" 'http://tkietwarana.ac.in/admission/PG-Programs' ">Click Here</a> </b>",

    "1.2",
    "<b>INFORMATION BROUCHRE<br>These are the top results: <br> <br> 1.2.1 Institute Brouchre<br> 1.2.2 UG Information Brouchre <br> 1.2.3 PG Information Brouchre</b>",
    "1.2.1",
    "<b > 1.2.1 Institute Brouchre<br>The link to Brouchre👉 <a href=" 'http://www.tkietwarana.ac.in/upload/admission/Institute%20Brochure%202021.pdf' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 UG Information Brouchre<br>The link to Brouchre👉<a href=" 'http://tkietwarana.ac.in/upload/admission/information%20brochure%202022-23.pdf' ">Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 PG Information Brouchre<br>The link to Brouchre👉 <a href=" 'http://tkietwarana.ac.in/upload/admission/Mtech%2022-23%20information%20brochure%202022-23.pdf' ">Click Here</a> </b>",

    "1.3",
    "<b>1.3 FIRST YEAR BTECH<br>These are the top results: <br> <br> 1.3.1 First year Details 👉 <a href=" 'http://www.tkietwarana.ac.in/upload/admission/Institute%20Broch'">click here</a><br> 1.3.2 Required Documents </b>",
    "1.3.2",
    "<b> 1.3.2 REQUIRED DOCUMENTS<br>The link to Notices👉 <a href=" 'http://tkietwarana.ac.in/upload/admission/22-23%20B.Tech-Required%20Documents%20List-2022-23.pdf' ">Click Here</a> </b>",

    "1.4",
    "<b > ADMISSION COMITTEE <br>The link to Admission comittee👉 <a href=" 'http://tkietwarana.ac.in/admission/admission-comittee' ">Click Here</a></b>",

    "2",
    "<b >DEPARTMENTS<br> Please select one from the options below :</br></br>2.1 Mechanical<br>2.2  Chemical<br>2.3  Computer Science<br>2.4  Electronics<br>2.5  Civil<br>2.6 Humanities and Science</b>",

    "2.1",
    "<b> The Mechanical Engineering Department is one of the prominent departments of Tatyasaheb Kore Institute of Engineering and Technology, belonging to Warana Educational Complex. It is established in the year 1996-97 initially with an intake capacity of 60 and increased to 120 in the year 2010-11. Further, the department added a Direct Second year division (II shift) with 60 intake capacity for Diploma students from 2011-12. Department has been accredited twice in April 2004 and September 2011 by the National Board of Accreditation (NBA), New Delhi. Department also runs Post Graduation Program in Design Engineering with an intake capacity of 18.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptmech/about-department' ">Click Here</a></b>",

    "2.2",
    "<b>Chemical engineering Department is established in the year of 1983 with 60 intakes for U.G. program. and PG program with 18 intakes from 1998.<br>Since from the establishment, the Department has gone for ISO certification, TEQUIP phase – II. UG program of Chemical Engineering Department has accredited by NBA – AICTE, New Delhi in 2004 for ‘5 years’ and in 2011 for ‘3 years’. Recently, the institute has accrediated by NAAC, Banglaru with CGPA 3.27 Grade 'A' and the department has approved recognized Ph.D center from June 2016-17 by Shivaji University, Kolhapur. Department has awarded 3rd rank at National Level for 'Best Industry Linked Department' by CII-AICTE, New Dehli for the year 2016-17. </b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptchem/about-department' ">Click Here</a></b>",
    "2.3",
    "<b>Computer Science Department is Established in 1999.Present Intake Capacity: 180.<br>Enriched Infrastructure Facilities.Ultra modern computing facilities with state-of-art laboratories.<br>Experienced, energetic, dedicated and devoted staff.<br>Accredited by the NBA in 2011.Ranked in Top 20 by AICTE- CII Survey in 2017.<br>Consistent 100% academic results.100+ Students placed in reputed MNC’s through campus interviews every year.<br>Active and Vibrant Professional bodies like Computer Society of India (CSI), Association of Computer Engineering Students (ACES).</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptcomp/About%20Us' ">Click Here</a></b>",
    "2.4",
    "<b>The Department of Electronics & Telecommunication Engineering established in the year 1983 is one of the premier departments in the college.  The Department offers an Under Graduate (UG)  with 60 intakes from 1983.  Department started Post Graduate (PG) program  in 1989 (Vacational) with 6 intake and regular  PG with 18 intake from 2010.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptelect/about-department' ">Click Here</a></b>",
    "2.5",
    "<b>The department of Civil engineering was established in the year 1983 initially with UG course in ‘Construction Technology’ with 60 intake capacity. Later shifted to UG course in Civil engineering with same intake in the year 1987. At present the department is has a intake capacity of 120 for the first year and 18 for PG in Construction and Management . The department is accredited two times by NBA-AICTE, New Delhi.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptcivil/about-department' ">Click Here</a></b>",
    "2.6",
    "<b>The Department of  Applied Science and Humanities was formed in  1990.  Dr.  S.  S.  Joshi was the first  Head of the Applied Science and Humanities department.   This department provides a breadth of knowledge in pure and basic sciences like Physics,    Chemistry,    Mathematics, and    English with engineering practices.  Applied Sciences  and  Humanities  subjects are the foundation subject for all disciplines such as     Mechanical,     Chemical,     Civil, Electronics and Telecommunication, and  Computer  Science  &  Engineering for Engineering and Technology.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dpthumanities/about-department' ">Click Here</a></b>",

    "5",
    "<b>Tatyasaheb Kore Institute of Engineering and Technology (TKIET) was established in 1983.The Institute is located at Warananagar, 30 km away from Kolhapur a district headquarter, and 10 km to the west from Kini-Wathar on Pune-Bangalore National Highway NH-4.TKIET has emerged as one of the leading technological institutes in Western Maharashtra.The Institute has a Lush-green campus spread over 30 acres in the picturesque foothill of Lord Jyotiba and historical Panhala Fort to the northeast.<br>For more info Please select one from the options below : <br> <br> 5.1 Vision Mission <br>5.2  Organisation structure<br>5.3  Infrastructure Details<br>5.4 Contact details <br></b>",
    "5.1",
    "<b>VISSION MISSION<br>For Vission And Mission👉 <a href=" 'http://tkietwarana.ac.in/about_tkiet/vision-mission' ">Click Here</a></b>",
    "5.2",
    "<b>ORGANISATION STRUCTURE<br>For Organisation Structure👉 <a href=" 'http://tkietwarana.ac.in/about_tkiet/Organisation-Structure' ">Click Here</a></b>",
    "5.3",
    "<b>INFRASTRUCTURE DETAILS<br>For Infrastructure Details is👉 <a href=" 'http://tkietwarana.ac.in/about_tkiet/Infrastructure-Details' ">Click Here</a></b>",
    "5.4",
    "<b>CONTACT DETAILS<br>For Contact details👉 <a href=" 'http://tkietwarana.ac.in/about_tkiet/Contact-us' ">Click Here</a></b>",

    "Tell me about Tkiet?",
    "<b>Tatyasaheb Kore Institute of Engineering and Technology (TKIET) was established in 1983.The Institute is located at Warananagar, 30 km away from Kolhapur a district headquarter, and 10 km to the west from Kini-Wathar on Pune-Bangalore National Highway NH-4.TKIET has emerged as one of the leading technological institutes in Western Maharashtra.The Institute has a Lush-green campus spread over 30 acres in the picturesque foothill of Lord Jyotiba and historical Panhala Fort to the northeast.",

    "Tell me about Mechanical Department?",
    "<b> The Mechanical Engineering Department is one of the prominent departments of Tatyasaheb Kore Institute of Engineering and Technology, belonging to Warana Educational Complex. It is established in the year 1996-97 initially with an intake capacity of 60 and increased to 120 in the year 2010-11. Further, the department added a Direct Second year division (II shift) with 60 intake capacity for Diploma students from 2011-12. Department has been accredited twice in April 2004 and September 2011 by the National Board of Accreditation (NBA), New Delhi. Department also runs Post Graduation Program in Design Engineering with an intake capacity of 18.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptmech/about-department' ">Click Here</a></b>",

    "Tell me about Chemical Department?",
    "<b>Chemical engineering Department is established in the year of 1983 with 60 intakes for U.G. program. and PG program with 18 intakes from 1998.<br>Since from the establishment, the Department has gone for ISO certification, TEQUIP phase – II. UG program of Chemical Engineering Department has accredited by NBA – AICTE, New Delhi in 2004 for ‘5 years’ and in 2011 for ‘3 years’. Recently, the institute has accrediated by NAAC, Banglaru with CGPA 3.27 Grade 'A' and the department has approved recognized Ph.D center from June 2016-17 by Shivaji University, Kolhapur. Department has awarded 3rd rank at National Level for 'Best Industry Linked Department' by CII-AICTE, New Dehli for the year 2016-17. </b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptchem/about-department' ">Click Here</a></b>",

    "Tell me about Computer Science Department?",
    "<b>Computer Science Department is Established in 1999.Present Intake Capacity: 180.<br>Enriched Infrastructure Facilities.Ultra modern computing facilities with state-of-art laboratories.<br>Experienced, energetic, dedicated and devoted staff.<br>Accredited by the NBA in 2011.Ranked in Top 20 by AICTE- CII Survey in 2017.<br>Consistent 100% academic results.100+ Students placed in reputed MNC’s through campus interviews every year.<br>Active and Vibrant Professional bodies like Computer Society of India (CSI), Association of Computer Engineering Students (ACES).</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptcomp/About%20Us' ">Click Here</a></b>",

    "Tell me about Electronics Department?",
    "<b>The Department of Electronics & Telecommunication Engineering established in the year 1983 is one of the premier departments in the college.  The Department offers an Under Graduate (UG)  with 60 intakes from 1983.  Department started Post Graduate (PG) program  in 1989 (Vacational) with 6 intake and regular  PG with 18 intake from 2010.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptelect/about-department' ">Click Here</a></b>",

    "Tell me about Civil Department?",
    "<b>The department of Civil engineering was established in the year 1983 initially with UG course in ‘Construction Technology’ with 60 intake capacity. Later shifted to UG course in Civil engineering with same intake in the year 1987. At present the department is has a intake capacity of 120 for the first year and 18 for PG in Construction and Management . The department is accredited two times by NBA-AICTE, New Delhi.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dptcivil/about-department' ">Click Here</a></b>",

    "Tell me about Humanities and Science Department?",
    "<b>The Department of  Applied Science and Humanities was formed in  1990.  Dr.  S.  S.  Joshi was the first  Head of the Applied Science and Humanities department.   This department provides a breadth of knowledge in pure and basic sciences like Physics,    Chemistry,    Mathematics, and    English with engineering practices.  Applied Sciences  and  Humanities  subjects are the foundation subject for all disciplines such as     Mechanical,     Chemical,     Civil, Electronics and Telecommunication, and  Computer  Science  &  Engineering for Engineering and Technology.</b><br><b>for  more info 👉 <a href=" 'http://tkietwarana.ac.in/dpthumanities/about-department' ">Click Here</a></b>",

]
# trainer.train("C:\\Users\\HP\\PycharmProjects\\chatbot3\\greetings.yml")
trainer.train(convo)


@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/")
# #def chatbot():
# return render_template("chatbot.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.debug = True
    app.run()