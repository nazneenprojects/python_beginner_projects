import typer
from rich.prompt import Prompt
from rich import print

app = typer.Typer(help=" CLI based CV for Nazneen Mulani")

@app.command()
def how_to_begin():
    print("----------------------------------------------------------------------------------")
    print("[yellow]Welcome to Nazneen's exploration journey! :")
    print("[green]Hope you are excited to dive in, lets begin!!!")
    person_name = Prompt.ask("Enter your name :sunglasses:")
    print(f"[red]Hey there, {person_name}!")
    print("[yellow]use different commands like <education>, <projects> ,<blogs> <hobbies> <career_journey> to know more onto specific section")
    print("..................................................................................")



@app.command()
def hobbies():
    print("----------------------------------When I am not working , I like to :------------------------------------------------")
    print("1. Explore different pathways of beautiful Earth with hiking, cycling, walking...")
    print("2. Painting Stones...")
    print("3. Reading Books...")
    print("----------------------------------------------------------------------------------")


@app.command()
def education():
    print("-------------------------------------education---------------------------------------------")
    print(
        """
        Master of Technology - Computer Science from Symbiosis International University [2015]
        - Research Thesis on Cloud Security
        - Research Details - implemented COBWEB algorithm for Cloud DB security to prevent Brute Force attack. 
        - Research paper presented in ICACCI conference 2015. Publications in - ScienceDirect & IJAER
        
        Bachelor of Engineering - Computer Science from Mumbai University [2012]
        - Volunteer for Student Editor Head for College Magazine in 2011
        """
    )

@app.command()
def projects():
    print("--------------------------------------projects--------------------------------------------")


@app.command()
def career_journey():
    print("-----------------------------------career_journey-----------------------------------------------")


@app.command()
def blogs():
    print("-----------------------------------career_journey-----------------------------------------------")

if __name__ == "__main__":
    #typer.run(main)
    app()