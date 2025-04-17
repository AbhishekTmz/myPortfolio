#dummy data
projects = {
    "Kids Learning App": {
        "name": "Kids Learning App",
        "short_description": "An engaging educational app for children aged 3–6 that teaches the alphabet through interactive games, voice-guided pronunciation, colorful animations, and fun tracing activities.",
        "Tech Stack": ["Flutter", "Dart", "Firebase"],
     "description": (
    "Kids Learning App is a fun and interactive Android application developed using Flutter and Dart, "
    "designed to support early childhood education for kids aged 3 to 6. The app combines colorful visuals, "
    "audio feedback, and hands-on activities to make alphabet learning an enjoyable experience. Children engage "
    "in drag-and-drop matching games that pair uppercase and lowercase letters, encouraging recognition through "
    "active play. "
    "Each interaction is enriched with delightful animations and sound effects, maintaining the child’s attention "
    "and fostering positive reinforcement. The app incorporates adaptive difficulty levels that adjust based on a "
    "child’s performance, ensuring the learning curve remains neither too easy nor too frustrating. "
    "A standout feature of the app is its voice pronunciation tool, powered by Flutter’s Text-to-Speech capabilities. "
    "This allows kids to tap on a letter and hear it spoken aloud in a friendly, clear voice—for example, “A for Apple”—"
    "helping develop both auditory and phonetic recognition. "
    "In addition to letter matching, the app offers tracing activities that help children develop fine motor skills and "
    "hand-eye coordination. These exercises use guided animations to teach proper stroke order, turning writing practice "
    "into an engaging mini-game. "
    "The app also features themed flashcards, animal associations, and a reward-based system that motivates children through "
    "progress tracking and badges. Designed with parental engagement in mind, the app provides progress insights and allows "
    "caregivers to monitor development. "
    "Overall, Kids Learning App is more than just a game—it’s a comprehensive early learning companion that builds foundational "
    "literacy skills in a safe, colorful, and encouraging environment."
),
        "images": {
            "main_image": "images/kids.jpg",
            "additional_images": ["images/shapes.JPEG" , "images/shapeee.JPEG"]
        }
    },

    "B Plus": {
        "name": "B Plus",
        "short_description": "A creator-focused media hub app that lets users explore, share, and engage with personalized content in a vibrant and interactive community environment",
        "Tech Stack": ["Flutter", "Dart", "Firebase", "REST API"],
        "description": (
            "B Plus is an Android-based media app with creator-focused tools that empower users to discover, share, "
            "and interact with personalized content in a vibrant, community-driven ecosystem."
        ),
        "images": {
            "main_image": "images/b plusss.webp",
            "additional_images": ["images/b plusss.webp" , "images/beee.JPEG"]
        }
    },

    "Global Cost of Living": {
        "name": "Global Cost of Living",
        "short_description": "An interactive Power BI dashboard that visualizes global cost of living, salaries, and housing affordability across continents, highlighting economic disparities and financial balance worldwide.",
        "Tech Stack": ["Kaggle Dataset", "Power BI"],
        "link": "",
        "description": (
            "This interactive dashboard provides a global overview of cost of living, average monthly net salaries, "
            "and housing affordability across continents and the top 10 countries. It shows that the United States leads "
            "with the highest average salary ($4K), followed by Canada and European countries, while Brazil and India are lower. "
            "A scatter plot shows a positive correlation between cost of living and salaries. The dashboard includes a world map, "
            "donut chart, and dual-axis line chart to illustrate the balance between income and expenses, highlighting disparities "
            "in affordability across different regions."
        ),
        "images": {
            "main_image": "images/costofliving.webp",
            "additional_images": ["images/dashss.jpg" , "images/scatterplot.jpg" , "images/mapp.jpg" , "images/linechart.jpg" , "images/stacked bar chart.jpg" , "images/dualline.jpg"     ]
        }
    },
    "My Personal Analytics Report": {
        "name": "My Personal Analytics Report",
        "short_description": "This infographic tracks 39 days of my business analytics student’s life. Key insights: most days involved class, some included work, and exercise was often intense. Study time averaged 4.82 hours, with a weak link between screen time and transactions. The student aims to cut screen time and boost exercise intensity.",
        "Tech Stack": ["Collected Personal Dataset ", "R studio" , "Canva"],
        "link": "https://www.canva.com/design/DAGTs5i3yWk/gHeFhF6EN_rkERNLB-C7yQ/edit?utm_content=DAGTs5i3yWk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton",
        "description": (
    "This infographic presents a personal data analysis titled 'My Life as a Business Analytics Student,' created using R Studio for analysis and Canva for design. "
    "The data was self-collected over 39 days and covers seven variables, including class attendance, workdays, exercise intensity, study hours, screen time, and transactions. "
    "Findings show that class was attended on 69.2% of days, work occurred on 33.3%, and most exercise sessions were at intensity level 4. "
    "Study hours averaged 4.82 per day with a right-skewed distribution, while screen time averaged 7.10 hours and transactions 2.82 per day, both left-skewed. "
    "A weak positive correlation (0.23) was found between screen time and transactions, while study hours remained largely unaffected by other variables. "
    "The infographic reflects how personal habits can be analyzed through data and visualized effectively, with key goals including reducing screen time and increasing exercise intensity."
),
        "images": {
            "main_image": "images/data.jpg",
            "additional_images": ["images/sc1.jpg" , "images/sc2.jpg." , "images/sc3.jpg"]
        }
    },

    "Auto SMS Sender": {
        "name": "Auto SMS Sender",
        "short_description": "A web app built with Flask and Twilio that sends an SMS featuring a random Harry Potter character when triggered through a user-friendly interface.",
        "Tech Stack": ["Twilio", "Flask", "Python", "HTML", "CSS"],
        "description": (
            "This SMS web application is built using Flask, HTML, and CSS, and uses the Twilio API to send text messages. "
            "When a user interacts with the web interface, the app fetches a random Harry Potter character from an external API "
            "and sends the character’s name to the user's phone via SMS. The project demonstrates API integration, "
            "Flask backend logic, and Twilio SMS capabilities."
        ),
        "images": {
            "main_image": "images/sms.jpg",
            "additional_images": ["images/sms.jpg"]
        }
    }
}
