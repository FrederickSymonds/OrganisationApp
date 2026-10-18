import customtkinter as ctk
import goalPage
import projectPage
import dayOrganiserPage
import reviewPage
import rulePage
import menuBar


class Gui(ctk.CTk):
    """
    This class is the main window that appears. It is responsible for controlling the link between the different pages and the main loop.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Different Frames
        self.menuBar = menuBar.MenuBar(self)
        self.goalFrame = goalPage.GoalPage(self)
        self.projectFrame = projectPage.ProjectPage(self)
        self.dayOrganiserFrame = dayOrganiserPage.DayOrganiserPage(self)
        self.reviewFrame = reviewPage.ReviewPage(self)
        self.ruleFrame = rulePage.RulePage(self)

        # Setting Variables
        self.dayStart = ctk.IntVar()
        self.dayStart.set(5)
        self.dayEnd = ctk.IntVar()
        self.dayEnd.set(21)

        # 

