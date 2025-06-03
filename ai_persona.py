import random

class AIPersona:
    
    def __init__(self):
        # Abhishek's actual information
        self.profile = {
            "name": "Abhishek Tamang",
            "title": "Business Analyst & Flutter Developer",
            "location": "Canada",
            "experience": "3+ years",
            "email": "atmz1113@gmail.com",
            "linkedin": "linkedin.com/in/abhishek-tamang-635668238/",
            "github": "github.com/AbhishekTmz"
        }
        
        # Abhishek's actual skills
        self.skills = {
            "frontend": ["HTML", "CSS", "JavaScript", "Bootstrap", "Responsive Design"],
            "backend": ["Python", "Flask", "Django", "Firebase", "REST APIs"],
            "mobile": ["Flutter", "Dart", "Cross-platform Development"],
            "database": ["Firebase", "MySQL", "SQLite"],
            "tools": ["Git", "VS Code", "Android Studio", "WordPress"],
            "analytics": ["Data Visualization", "Business Intelligence", "Statistical Analysis", "Power BI"],
            "languages": ["Python", "Dart", "JavaScript", "PHP"]
        }
        
        # Abhishek's actual projects and experience
        self.projects = [
            {
                "name": "Flutter Mobile Applications",
                "description": "Cross-platform mobile apps built with Flutter and Firebase integration",
                "tech": ["Flutter", "Dart", "Firebase", "REST APIs"],
                "role": "Flutter Developer at Kitwosd IT Support Center"
            },
            {
                "name": "WordPress Development",
                "description": "Custom WordPress websites with responsive design and SEO optimization",
                "tech": ["WordPress", "PHP", "CSS", "JavaScript"],
                "role": "Junior WordPress Developer"
            },
            {
                "name": "Business Analytics Projects",
                "description": "Data analysis and visualization projects for business insights",
                "tech": ["Python", "Power BI", "Statistical Analysis", "Data Visualization"],
                "role": "Business Analytics Student at Cambrian College"
            }
        ]
        
        # Conversation patterns and responses
        self.greetings = [
            "Hi there! I'm the AI version of {name}. How can I help you learn more about my background?",
            "Hello! Welcome to my portfolio. I'm here to answer any questions about my experience and skills.",
            "Hey! I'm {name}'s AI assistant. What would you like to know about my projects or background?"
        ]
        
        self.conversation_context = []
    
    def get_response(self, message):
        message = message.lower().strip()
        
        # Store conversation context
        self.conversation_context.append(message)
        
        # Greeting responses
        if any(word in message for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(self.greetings).format(name=self.profile["name"])
        
        # About/profile questions
        elif any(word in message for word in ['about', 'who are you', 'introduce', 'background']):
            return f"I'm {self.profile['name']}, a {self.profile['title']} with {self.profile['experience']} of experience. I'm currently based in {self.profile['location']} and have a strong foundation in data analytics, business intelligence, and mobile app development. I'm passionate about transforming data into meaningful insights and building cross-platform applications with Flutter."
        
        # Skills questions
        elif any(word in message for word in ['skills', 'technologies', 'tech stack', 'programming']):
            return self.format_skills_response()
        
        # Projects questions
        elif any(word in message for word in ['projects', 'work', 'portfolio', 'built', 'created']):
            return self.format_projects_response()
        
        # Experience questions
        elif any(word in message for word in ['experience', 'career', 'job', 'work history']):
            return f"I have {self.profile['experience']} of professional development experience. I currently work as a Flutter Developer at Kitwosd IT Support Center, building cross-platform apps with Flutter, Firebase, and REST APIs. Previously, I was a Flutter Developer Intern at Big Studio and worked as a Junior WordPress Developer. I'm also pursuing Business Analytics at Cambrian College, focusing on data analysis and visualization."
        
        # Contact questions
        elif any(word in message for word in ['contact', 'email', 'reach', 'hire', 'availability']):
            return f"I'd love to connect! You can reach me at {self.profile['email']} or connect with me on LinkedIn at {self.profile['linkedin']}. I'm always open to discussing new opportunities and interesting projects."
        
        # Specific technology questions
        elif any(tech.lower() in message for tech in ['flutter', 'dart', 'firebase', 'python', 'wordpress', 'analytics']):
            return self.get_tech_specific_response(message)
        
        # Default responses
        else:
            fallback_responses = [
                "That's an interesting question! Could you be more specific about what you'd like to know about my background, skills, or projects?",
                "I'd be happy to help! You can ask me about my experience, technical skills, projects, or how to get in touch.",
                "I'm here to share information about my professional background. Feel free to ask about my projects, skills, experience, or contact details!",
                "Great question! I can tell you about my technical expertise, past projects, career experience, or how we might work together."
            ]
            return random.choice(fallback_responses)
    
    def format_skills_response(self):
        response = f"I work with a diverse tech stack spanning mobile development, web development, and data analytics! Here's what I specialize in:\n\n"
        response += f"📱 Mobile: {', '.join(self.skills['mobile'])}\n"
        response += f"🎨 Frontend: {', '.join(self.skills['frontend'])}\n"
        response += f"⚙️ Backend: {', '.join(self.skills['backend'])}\n"
        response += f"📊 Analytics: {', '.join(self.skills['analytics'])}\n"
        response += f"🗄️ Databases: {', '.join(self.skills['database'])}\n"
        response += f"🛠️ Tools: {', '.join(self.skills['tools'])}\n\n"
        response += "I'm currently pursuing Business Analytics while working as a Flutter Developer, combining my passion for mobile development with data-driven insights!"
        return response
    
    def format_projects_response(self):
        response = "Here are some of my key projects and experiences:\n\n"
        for i, project in enumerate(self.projects, 1):
            response += f"{i}. **{project['name']}**\n"
            response += f"   {project['description']}\n"
            response += f"   Tech: {', '.join(project['tech'])}\n"
            response += f"   Role: {project['role']}\n\n"
        response += "I also have experience with WordPress development and am currently working on business analytics projects. Would you like to know more about any specific project or technology?"
        return response
    
    def get_tech_specific_response(self, message):
        tech_responses = {
            'flutter': "Flutter is my primary mobile development framework! I use it to build cross-platform apps for both iOS and Android. At Kitwosd IT Support Center, I work with Flutter, Firebase, and REST APIs to create seamless mobile experiences.",
            'dart': "Dart is the programming language I use for Flutter development. I love its strong typing system and how it compiles to native code for great performance on mobile devices.",
            'firebase': "Firebase is my go-to backend solution for mobile apps! I use it for authentication, real-time databases, cloud storage, and push notifications in my Flutter projects.",
            'python': "Python is essential for my business analytics work! I use it for data analysis, statistical modeling, and automation scripts. It's also great for web development with Flask.",
            'wordpress': "I worked as a Junior WordPress Developer, customizing themes, managing plugins, and building responsive websites. I focused on creating SEO-friendly, fast, and user-friendly experiences.",
            'analytics': "Business Analytics is my current focus at Cambrian College! I work with data visualization, statistical analysis, and business intelligence tools like Power BI to transform data into actionable insights."
        }
        
        for tech, response in tech_responses.items():
            if tech in message:
                return response
        
        return "I'd be happy to discuss any of my technical skills in detail! I work with Flutter, Python, WordPress, Firebase, and various analytics tools."
