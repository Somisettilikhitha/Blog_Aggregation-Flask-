from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('categories.html')

@app.route('/c')
def c_category():
    category_name = 'C'
    blog_content = [
        ('1.PROGRAMIZ', 'https://www.programiz.com/c-programming'),
        ('2.W3 SCHOOLS', 'https://www.w3schools.com/c/c_intro.php'),
        ('3.JAVA POINT', 'https://www.javatpoint.com/c-programming-language-tutorial'),
        ('4.GREEK FOR GREEKS', 'https://www.geeksforgeeks.org/c-programming-language/'),
        ('5.TUTORIAL POINTS', 'https://www.tutorialspoint.com/cprogramming/index.htm'),
        ('6.FREE CODE CAMP', 'https://www.freecodecamp.org/news/what-is-the-c-programming-language-beginner-tutorial/'),
        ('7.SCALER', 'https://www.scaler.com/topics/c/'),
        ('8.BEGINNERS BOOK', 'https://beginnersbook.com/2014/01/c-tutorial-for-beginners-with-examp'),
        ('9.LOG2BASE2', 'https://www.log2base2.com/C/basic/simple-c-program.html'),
        ('10.C PROGRAMMING.COM', 'https://www.cprogramming.com/tutorial/c-tutorial.html?inl=hp')
    ]
    return render_template('empty_page.html', category_name=category_name, blog_content=blog_content)

@app.route('/python') 
def python_category():
    category_name = 'Python'
    blog_content = [
        ('1.PROGRAMIZ', 'https://www.programiz.com/python-programming'),
        ('2.W3 SCHOOLS', 'https://www.w3schools.com/python/python_intro.asp'),
        ('3.JAVA POINT', 'https://www.javatpoint.com/python-tutorial'),
        ('4.GREEK FOR GREEKS', 'https://www.geeksforgeeks.org/python-programming-language/'),
        ('5.PYTHON TUTORIAL', 'https://www.pythontutorial.net/'),
        ('6.FREE CODE CAMP', 'https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/'),
        ('7.SCALER', 'https://www.scaler.com/topics/python/'),
        ('8.INTELLIPAAT', 'https://intellipaat.com/blog/tutorial/python-tutorial/'),
        ('9.DIGITAL OCEAN', 'https://www.digitalocean.com/community/tutorial-series/how-to-code-in-python-3'),
        ('10.QUANTLNSTI', 'https://blog.quantinsti.com/python-programming/')
    ]
    return render_template('empty_page.html', category_name=category_name, blog_content=blog_content)

@app.route('/java')
def java_category():
    category_name = 'Java'
    blog_content = [
        ('1.W3 SCHOOLS', 'https://www.w3schools.com/java/java_intro.asp'),
        ('2.PROGMAIZ', 'https://www.programiz.com/java-programming'),
        ('3.JAVA POINT', 'https://www.javatpoint.com/java-tutorial'),
        ('4.GREEK FOR GREEKS', 'https://www.geeksforgeeks.org/java/'),
        ('5.JAVA TUTORIAL', 'https://www.tutorialspoint.com/java/'),
        ('6.SCALER', 'https://www.scaler.com/topics/java/'),
        ('7.GURU99', 'https://www.guru99.com/java-tutorial.html'),
        ('8.CODE WITH HARRY', 'https://www.codewithharry.com/tutorial/java/'),
        ('9.WIKI BOOKS', 'https://en.wikibooks.org/wiki/Java_Programming'),
        ('10.LEARN JAVA ONLINE','https://www.learnjavaonline.org/')
    ]
    return render_template('empty_page.html', category_name=category_name, blog_content=blog_content)

@app.route('/sports')
def sports_category():
    category_name = 'Sports'
    blog_content = [
        ('1.BBCI', 'https://www.bcci.tv/'),
        ('2.MARCA', 'https://www.marca.com/'),
        ('3.CRICBUZZ', 'https://www.cricbuzz.com/CRICBUZZ'),
        ('4.AS', 'https://as.com/'),
        ('5.ESPNCRICINFO', 'https://www.espncricinfo.com/'),
        ('6.SPORTSKEEDA', 'https://www.sportskeeda.com/'),
        ('7.GOAL', 'https://www.goal.com/en-in'),
        ('8.YAHOO SPORTS', 'https://sports.yahoo.com/'),
        ('9.247SPORTS', 'https://247sports.com/'),
        ('10.ESPN','https://www.espn.in/')
    ]
    return render_template('empty_page.html', category_name=category_name, blog_content=blog_content)

@app.route('/politics')
def politics_category():
    category_name = 'Politics'
    blog_content = [
        ('1.TIMES OF INDIA', 'https://timesofindia.indiatimes.com/blogs/politics/'),
        ('2.NIC', 'https://www.nic.in/'),
        ('3.PRESIDENT OF INDIA', 'https://presidentofindia.nic.in/'),
        ('4.THE HINDU', 'https://www.thehindu.com/news/national/andhra-pradesh/'),
        ('5.', ''),
        ('6.', ''),
        ('7.', ''),
        ('8.', ''),
        ('9.', ''),
        ('10.','')
    ]
    return render_template('empty_page.html', category_name=category_name, blog_content=blog_content)

if __name__ == '__main__':
    app.run(debug=True)
