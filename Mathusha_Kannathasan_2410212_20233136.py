import time
import random

# Initialize variables to store selected_projects and totalScore
selected_projects = {}
totalScore = {}

# Initialize an empty list to store projects_list
projects_list = []

print("\n*********TechExpo*********")
time.sleep(2)
print("----Welcome to TechExpo----")
time.sleep(2)
print()

#################################################################################################################
#Adding Project Details (APD)
#Allow the participants to input their project details

def APD():
    time.sleep(1)
    print("--Now you can add your project details--")
    while True:
        time.sleep(1)
        print()
        project_ID = input("Enter your project ID:")
        try:
            project_ID = int(project_ID)
            #Check whether the id already exists
            if project_ID in {project["project_ID"] for project in projects_list}:
                time.sleep(2)
                print()
                print("--The project Id is already exist in the list, please enter a unique ID--")
            else:
                time.sleep(1)
                print("---Hurray!!! Your ID is unique---")
                #Input project details
                project_name = input("Enter your project name:").capitalize()
                #Validate category input
                while True:
                    category = input("Enter the category to which your project belongs (AI/RT/ML):").upper()
                    if category in {"AI", "ML", "RT"}:
                        break
                    else:
                        print("Invalid category! Please enter (Al/ML/RT).")
                # Input team members' names with validation for exactly 3 members
                while True:
                    team_members = [name.capitalize()
                                    for name in input("Enter your team members' names:").split(",")]
                    if len(team_members) == 3:
                        break
                    else:
                        print("Please enter exactly three team members.")
                brief_description = input("Enter a brief description about the project:").capitalize()
                country = input("Enter your country:").capitalize()
                #Create a dictionary to input the user's details
                new_project = {"project_ID": project_ID,
                               "project_name": project_name, 
                               "category": category,
                               "team_members": team_members,
                               "brief_description": brief_description,
                               "country": country}   
                # Append the project details to the projects list
                projects_list.append(new_project)
                time.sleep(2)
                print("\n--Project details have been added successfully--\n")
                SPD()
                break
            time.sleep(1)
        except ValueError:
            print("Invalid input! Please enter a valid integer for project_ID.")
    

#################################################################################################################
#Deleting Project Details(DPD)
#Here the user can delete the unwanted project by finding the projects using the project ID
    
def DPD():
    time.sleep(1)
    print("Think twice.... Will you intend to delete your project?")
    print("--If you delete your project, then you can not participate--")
    print()
    time.sleep(2)
    decision = input("Do you want to delete your project? (yes/no):")
    print()
    if decision.lower() == "yes":
        time.sleep(1)
        while True:
            delproid = input("Enter the project ID you want to delete:")
            try:
                delproid = int(delproid)
                print()
            except ValueError:
                print("Invalid input! Please enter a valid integer for project_ID.")
                print()
                continue
            #Check whether the id already exists 
            for project in projects_list:
                if delproid == project["project_ID"]:
                    #Remove the project from the projects list
                    projects_list.remove(project)
                    time.sleep(1)
                    print(f"Project with ID {delproid} has been successfully deleted.")
                    print()
                    SPD()
                    break
            else:
                print(f"Project with ID {delproid} is not found in our list.")
            break
    elif decision.lower() == "no":
        print("You can participate, your project details will not be deleted.")
    else:
        print("Invalid option. Please enter 'yes' or 'no'.")
    time.sleep(1)
    print()


#################################################################################################################
#Updating Project Details(UPD)
#Here the project details can be updated by finding the projects using project ID
    
def UPD():
    time.sleep(1)
    print("Are you really want to update?")
    print("If you update your details, then your previous details will be updated.")
    print()
    time.sleep(1)
    option = input("Do you want to update your project details? (yes/no):")
    print()
    if option.lower() == "yes":
        time.sleep(1)
        while True:
            updateproid = input("Enter the project ID of the project you want to update:")
            try:
                updateproid = int(updateproid)
                print()
            except ValueError:
                print("Invalid input! Please enter a valid integer for project_ID.")
                continue
            #Check whether the ID already exists and update the details
            for project in projects_list:
                if updateproid == project["project_ID"]:
                    print("Now, you can update the details.")
                    print()
                    time.sleep(1)
                    #Update details seperately
                    project["project_name"] = input("Enter the updated project name:").capitalize()
                    # Validate category input
                    while True:
                        category = input("Enter the updated category (AI/RT/ML):").upper()
                        if category in ["AI", "RT", "ML"]:
                            project["category"] = category
                            break
                        else:
                            print("Invalid category! Please enter (AI/ML/RT).") 
                            #Input team members' names exactly 3 members
                    while True:
                        team_members = [name.capitalize()
                                        for name in input("Enter your team members' names: ").split(",")]
                        if len(team_members) == 3:
                            project["team_members"] = team_members
                            break
                        else:
                            print("Please enter exactly three team members.")
                    project["brief_description"] = input("Enter the updated brief description about the project:").capitalize()
                    project["country"] = input("Enter the updated country:").capitalize()
                    print()
                    print("Project details has been updated successfully.")
                    print()
                    SPD()
                    break
            else:
                print("Project with ID", updateproid, "is not found in our list.")
            break
    elif option.lower() == "no":
        print("You can participate, your project details will not be updated.")
    else:
        print("Invalid option. Please enter 'yes' or 'no'.")
    time.sleep(1)
    print()


#################################################################################################################
#Viewing Project Details(VPD)
#Here the inserted projects will be listed in ascending order based on the project_ID
    
def VPD():
    time.sleep(1)
    print("--The project details will be displayed in ascending order based on project_ID--")
    time.sleep(2)
    print()
    if len(projects_list) == 0:
        print("The projects has not been added yet now.")
    else:
        sorted_list = []
        for i in range(len(projects_list)): #outer loop
            for j in range(i +1, len(projects_list)): #inner loop
                if projects_list[i]["project_ID"] > projects_list[j]["project_ID"]:
                    #Swap the order in ascending, like min(project_ID), max(project_ID)
                    projects_list[i], projects_list[j] = projects_list[j], projects_list[i]

        for project in projects_list:
            #Format project details for display
            proDetails= {"project_ID": project["project_ID"],
                         "project_name": project["project_name"],
                         "category": project["category"],
                         "team_members": project["team_members"],
                         "brief_description": project["brief_description"],
                         "country": project["country"]}
            sorted_list.append(proDetails)
        time.sleep(1)
        for project in sorted_list:  # Iterate through sorted_list to print each project's details on a new line
            print(project)
            print()
    time.sleep(1)
    print()


#################################################################################################################
# Saving Project Details to Text File(SPD)
# Here the project details will be saved into a text file.
def SPD():
    time.sleep(1)
    if len(projects_list) == 0:
        print("The projects have not been added yet.")
        print()
        EXIT()
    else:
        print("--Saving project details to text file...")
        print()
        time.sleep(1)
        # Initialize dictionaries to store project details by category
        categories = {"AI": [], "RT": [], "ML": []}
        for project in projects_list:
            # Append project details to the respective category list
            categories[project["category"]].append(project)
        try:
            with open("project_details.txt", "w") as file: # Open file in append mode
                for category, projects in categories.items():
                    file.write("\n")
                    file.write(f"*********** {category} Projects ***********\n")
                    file.write("\n")
                    for project in projects:
                        # Write project details to the text file
                        file.write("---Project Details---\n")
                        file.write(f"Project ID: {project['project_ID']}\n")
                        file.write(f"Project Name: {project['project_name']}\n")
                        file.write(f"Category: {project['category']}\n")
                        # Join team members using ','
                        file.write(f"Team Members: {', '.join(project['team_members'])}\n")
                        file.write(f"Brief Description: {project['brief_description']}\n")
                        file.write(f"Country: {project['country']}\n")
                        file.write("\n")
                print("Project details saved to 'project_details.txt' successfully.")
                print()
        except IOError:
            print("Error: Unable to access the file.")
            print()
            EXIT()


#################################################################################################################
#Random Spotlight Selection(RSS)
#3 cateogories are assigned. Here One project has been randomly selected from each category.
    
def RSS():
    try:
        time.sleep(1)
        with open("project_details.txt", "r") as file:
            # Read all lines from the file
            lines = file.readlines()

        # Initialize empty dictionaries to store projects for each category
        categories = {"AI": {}, "RT": {}, "ML": {}}

        # Iterate through lines to extract project details
        project_details = {}
        for line in lines:
            # Strip removes any leading whitespace
            line = line.strip()
            # Check if the line contains a colon to split into key-value pairs
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                # Split the current line at the first occurrence of ":" and limit to only one
                # and strip whitespace from both parts
                project_details[key] = value
            else:
                # If line doesn't contain a colon, it might be the start of a new project section
                # If project details exist, add them to the appropriate category
                if project_details:
                    category = project_details.get("Category")
                    if category in categories:
                        categories[category][project_details["Project ID"]] = project_details
                    # Reset project details dictionary for the next project
                    project_details = {}

        # Randomly select one project from each category
        print("--Randomly selected projects will be listed down--")
        print()
        time.sleep(1)
        for category, projects in categories.items():
            if projects:  # Check if there are projects in the category
                selected_projects[category] = random.choice(list(projects.values()))
                print(f"--Randomly Selected Project Details ({category}):")
                # Display randomly selected project details of each category
                for key, value in selected_projects[category].items():
                    print(f"{key}: {value}")
                time.sleep(1)
                print()
            else:
                print(f"No projects found in category {category}.")

        return selected_projects              

    except FileNotFoundError:
        print("Project details file not found.")
        EXIT()
        
    print()


#################################################################################################################
#Awards Winning Projects(AWP)
#Take points from four judges for each selected project, calculate total scores,
#and determine overall 3 winners for 1st, 2nd, and 3rd place.
    
def AWP(selected_projects):
    # Initialize scores list
    scores = []
    time.sleep(1)
    print("--Judges can enter score for selected projects now--")
    time.sleep(1)
    # Iterate through selected projects to determine scores
    for category, project in selected_projects.items():
        # Initialize total score for the current project
        total_score = 0
        print(f"\n---Scoring project of ({category}) with project_ID- {project['Project ID']}:")
        # Take scores from four judges
        for judge in range(1, 5):
            # Initialize flag for valid input
            valid_input = False
            while not valid_input:
                # Prompt the judge for a score using stars
                rating = input(f"Judge {judge}: Enter rating using stars only (1-5):")
                # Validate input and convert stars to numerical score
                score = len(rating)
                try:
                    if rating.count("*") < 1 or rating.count("*") > 5:
                        raise ValueError
                    total_score += rating.count("*")  #Assign the count of '*' as the score
                    valid_input = True
                except ValueError:
                    print("Invalid input! Please enter between 1 and 5 '*' characters.")
        print(f"Total score for project ({category}) with project_ID- {project['Project ID']} is: {total_score}")
        time.sleep(1)
        # Append total score to scores list
        scores.append((category, project['Project ID'], total_score))
        # Store total score in totalScore dictionary along with place_info
        place_info = None  # Initialize place_info
        totalScore[project['Project ID']] = {"Total Score": total_score,
                                             "Place Info": place_info,
                                             "Project Details": project}
              
    # Initialize variables to store the first, second, and third places
    first_place = None
    second_place = None
    third_place = None     
    # Iterate through scores to find the first, second, and third places
    for score in scores:
        if first_place is None or score[2] > first_place[2]:
            third_place = second_place
            second_place = first_place
            first_place = score
        elif second_place is None or score[2] > second_place[2]:
            third_place = second_place
            second_place = score
        elif third_place is None or score[2] > third_place[2]:
            third_place = score
        # Handle ties
        elif score[2] == first_place[2]:  # Tie with first place
            first_place = random.choice([first_place, score])
        elif score[2] == second_place[2]:  # Tie with second place
            second_place = random.choice([second_place, score])
        elif score[2] == third_place[2]:  # Tie with third place
            third_place = random.choice([third_place, score])              
    # Assign places in totalScore dictionary
    if first_place:
        totalScore[first_place[1]]["Place Info"] = "1st Place"
    if second_place:
        totalScore[second_place[1]]["Place Info"] = "2nd Place"
    if third_place:
        totalScore[third_place[1]]["Place Info"] = "3rd Place"         
    # Display overall ranking
    print("\n---Overall Ranking:")
    print()
    time.sleep(3)
    if first_place:
        print(f"1st Place: Category-({first_place[0]}) Project_ID-({first_place[1]}) with {first_place[2]} points")
        time.sleep(2)
        if second_place:
            print(f"2nd Place: Category-({second_place[0]}) Project_ID-({second_place[1]}) with {second_place[2]} points")  
            time.sleep(1)
            if third_place:
                print(f"3rd Place: Category-({third_place[0]}) Project_ID-({third_place[1]}) with {third_place[2]} points")  
    # Create a list of place tuples
    place_info = [first_place, second_place, third_place]    
    return totalScore
    time.sleep(1)


#################################################################################################################
# Visualizing Award-Winning Projects (VAP)
# Here the awards will be visualized using "*"

def VAP(totalScore):
    print()
    time.sleep(1)
    print("---Hereafter, Awards for the winning projects will be visualized---")
    print()
    time.sleep(2)
    
    # Define a list to store the place information
    places = ["1st Place", "2nd Place", "3rd Place"]
    
    # Iterate through places
    for place in places:
        # Iterate through totalScore dictionary to find projects for the current place
        for project_id, project_info in totalScore.items():
            if project_info["Place Info"] == place:
                print("\n".join(["  *" for _ in range(project_info["Total Score"])]))
                print(project_info["Project Details"]["Project Name"])
                print(project_info["Project Details"]["Country"])
                print(project_info["Place Info"])
                print()
                time.sleep(2)
    time.sleep(1)


#################################################################################################################
#Function to terminate the program(EXIT)
    
def EXIT():
    time.sleep(1)
    print("--Exiting the program...")
    print("Thank you for participating in TechExpo. Have a great day!")
    exit()  # Exit the program

    
#################################################################################################################

def main_menu():
    while True:
        print("--Select your choice from the following menu:")
        print()
        time.sleep(2)
        print("1. Adding Project Details (APD)")
        print("2. Deleting Project Details (DPD)")
        print("3. Updating Project Details (UPD)")
        print("4. Viewing Project Details (VPD)")
        print("5. Saving Project Details to Text File (SPD)")
        print("6. Random Spotlight Selection (RSS)")
        print("   Recording Awards and Recognitions (AWP)")
        print("   Visualizing Award-Winning Projects (VAP)")
        print("   Exiting the Program (EXIT)")
        print()
        time.sleep(1)
        choice = input("Enter your choice (1 to 6): ")

        match choice:
            
            case "1":
                print()
                APD()

            case "2":
                print()
                DPD()

            case "3":
                print()
                UPD()

            case "4":
                print()
                VPD()

            case "5":
                print()
                SPD()

            case "6":
                print()
                RSS()  #Call RSS()
                print()
                AWP(selected_projects)  # Call AWP(selected_projects)
                print()
                VAP(totalScore)  # Call VAP(totalScore)
                print()
                EXIT()  # Call EXIT()
                break
            
            case _:
                print("Invalid choice. Please enter the valid input.")
                print()

main_menu()

#################################################################################################################
