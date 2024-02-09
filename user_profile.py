# user_profile.py

import sys, os.path
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont, QPixmap


class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()
        
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.displayImages()
        self.displayUserInfo()
        
        self.show()
        
    def displayImages(self):
        """
        Display background and profile images.
        Check to see if image files exist, if not throw an exception.
        """
        background_image = "images/skyblue_background.png"
        profile_image = "images/profile_image.jpg"
        
        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found.")
            

        try:
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.setMaximumHeight(145)
                user_image.move(30, 0)
        except FileNotFoundError:
            print("Image not found.")
            
    
    def displayUserInfo(self):
        """
        Create the labels to be displayed for the User Profile.
        """
        
        user_name = QLabel(self)
        user_name.setText("John Doe")
        user_name.move(80, 140)
        user_name.setFont(QFont("Arial", 20))
        
        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15, 170)
        bio_title.setFont(QFont("Arial", 17))
        
        about = QLabel(self)
        about.setText("\nI'm a Software Engineer with 8 years\
                      experiece creating awesome code.")
        about.setWordWrap(True)
        about.move(15, 190)
        
        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15, 240)
        skills_title.setFont(QFont("Arial", 17))
        
        skills = QLabel(self)
        skills.setText("\nPython  |  PHP  |  SQL  |  JavaScript")
        skills.move(15, 260)
        
        experience_title = QLabel(self)
        experience_title.setText("Experience")
        experience_title.move(15, 290)
        experience_title.setFont(QFont("Arial", 17))
        
        experience = QLabel(self)
        experience.setText("\nPython Developer")
        experience.move(15, 310)
        
        dates = QLabel(self)
        dates.setText("Mar 2011 - Present")
        dates.move(15, 333)
        dates.setFont(QFont("Arial", 10))
        
        experience = QLabel(self)
        experience.setText("\nPizza Delivery Driver")
        experience.move(15, 350)
        
        dates = QLabel(self)
        dates.setText("Aug 2015 - Dec 2017")
        dates.move(15, 373)
        dates.setFont(QFont("Arial", 10))
        

# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserProfile()
    sys.exit(app.exec_())