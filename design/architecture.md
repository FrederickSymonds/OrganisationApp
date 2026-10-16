Based on System.md.
0. Base - What main navigation looks like.
1. Project Manager - Manage goals, projects and tasks fluid-like.
2. Day Organiser - Loads routine tasks and scheduled tasks, then can fill with rest
3. Review System - mark down short and long comments on projects, goals and days
4. Rule System - Just a nice display of rules, easy to see and edit and track how many days they have been followed.
## 0. Base
**Gui**
- Thin bar at the top, with 'home', 'settings', 'Help'. (Simple for now)
	- home - gives drop down for main 1-4. 
	- settings - popup menu with options in it
	- help - key information popup

## 1. Project Manager
#### Data Structures;
**Life Goals**
- Title - TEXT
- Description - TEXT
- Objectives - TEXT
- Colour - TEXT (hex/...)
- Picture - TEXT (file name for image)
- ID - INT (autoincrement)

**Goals**
- Title - TEXT
- Description - TEXT
- Objectives - TEXT
- Colour - TEXT (hex/...)
- ID - INT (autoincrement)
- Life Goal ID - INT
- Status - TEXT

**Projects**
- Title - TEXT
- Description - TEXT
- Objectives - TEXT
- ID - int (autoincrement)
- Goal ID - INT
- Status - TEXT

**Work Tasks**
- Title - TEXT
- Objectives - TEXT
- ID - int (autoincrement)
- proj ID - INT
- Status - TEXT

#### GUI
**Life Goals**
See below, life goals and goals are joint.

**Goals**
Graph View, Life goals in centre and goals surrounding them, click for more details. They should be ellipse shape. When clicked on, full details on the right. The reason for this design choice, is to make it clear where each goal comes from, in a clear manner. They also don't change very frequently, so as stuck with the same goals for a long time, you can grow more accustomed to the layout.
![Goal Page Design](https://github.com/FrederickSymonds/OrganisationApp/blob/main/design/images/ProjectManager1.jpg)
**Projects**
Card view, however grouped by life goals, then by goals. Click for more details on the right. This was chosen, as there can be many projects on at a single time, and more information is displayable, and as project come and go, it's good to see critical information quickly, to know which one is which.
![Project Manager Design](https://github.com/FrederickSymonds/OrganisationApp/blob/main/design/images/ProjectManager2.jpg)
**Work Tasks**
Only viewable through project view. Next task in project viewable on card, but the rest must click on the card.

#### Other Design options
- Use arrow keys to quickly change between these 3 page views
- e = Edit current selected
- a = Add new (shift + a for task/project/goal?)
- D = delete, capital just to make sure
- Preload left side, but leave right side empty. For speed.
## 2. Day Organiser
**GUI**
Similar to a normal calendar app, but with 1 day on it (Extension: see multiple days). It then fills it with routine tasks, and scheduled tasks, then allows for schedules/work tasks to be placed in, using a popup menu.
![Day Organiser Page Design](https://github.com/FrederickSymonds/OrganisationApp/blob/main/design/images/DayOrganiser.jpg)

**Settings**
- Sleep Times (Changes when day begins and ends)
- Block Times (Changes start and end time of blocks, to allow for integration with odd times).
	- If 2 of same block in a row, then merge.
- Optional line to indicate current time / where at right now.

**Data** (Alongside Project Manager data)
- Year (To update routine tasks every year)

Routine Tasks
- Title - TEXT
- Colour - TEXT
- ID - INT (autoincrement)
- Time of day - TEXT
- Reoccurance - TEXT (eg. (1 mod 2), (3, 4, 5 mod 7), so x mod y, updated every year)
- Length - INT (How much time)
- Status - BOOL/INT (Resets every day)

Scheduled Tasks
- Title - TEXT
- Objectives - TEXT (Optional, depending on how complex task is)
- ID - INT (autoincrement)
- Time set - STR (Datetime, can be Null)
- Deadline - STR (Date)
- Length - INT (How much time)
- Status - BOOL/INT

**Other Design Options**
- Arrow keys control days
- r = routine task page
- a = add (Scheduled task)
## 3. Review(Journal) System

**GUI**
Appears like a chat log, but your the only person on it. These can be short comments about a project, or a long summary of a day. It comes with a side panel for filtering, changing between edit and viewing mode (to be able to edit any viewable).

![Review Page Design](https://github.com/FrederickSymonds/OrganisationApp/blob/main/design/images/ReviewSystem.jpg)

**Data Structure**
Message
- Datetime - TEXT (When posted)
- Message - TEXT
- Type - TEXT (proj/goal/day/week/rule..... + their ID) 
- ID - INT (autoincrement)

**Other Design Options**
- a = add
- e = edit
## 4. Rule System
**GUI**
Ordered list of rules, with most important near the top (can easily change order). Each rule is listed clearly, and has a days since last broken, and a 'I have broken' button, which will require a review message, entering why I broke it and what led up to it, to help prevent it in the future.

![Rule System Page Design](https://github.com/FrederickSymonds/OrganisationApp/blob/main/design/images/RuleSystem.jpg)

**Data Structure**
Rule
- Title - TEXT
- Last Broken - TEXT (datetime)
- Order - INT (Relative to other rules)
- ID - INT (autoincrement)

**Other Design Options**
- when click on a rule, it becomes selected
- arrow keys to move selected
- e = edit selected
- D = delete selected
- a = add (Scheduled task)

## Extensions (Future)

- Track ratios of tasks being done, by goals/... and use to decide where to put time.
- Text editor / Obsidian replacement (Mathematics specific)
- Automatically update google calendar
- Allow the ability to see past projects/goals/tasks?
