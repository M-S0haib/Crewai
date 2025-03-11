from crewai import Agent, Crew, Task

class Mathematical_Crew:

    GEMINI_API_KEY = "AIzaSyD12aBZi7281iDeQGb9qYVMm8wr_TBvyqE"



    def __init__(self):
        self.Math_problem_solver_agent = Agent(
            role="A Mathematician",
            goal="Have a normal conversation with the user. Reply to user questions. Give user solutions to the mathematical problems whenever he asks. ",
            backstory="An experienced mathematician that helps users solve mathematical problems.",
            verbose=True,
            memory=True,        )

        self.Math_problem_solving_task = Task(
            description="Have a normal conversation with the user. Reply to user questions. Give user solutions to the mathematical problems {user_input} whenever he asks.if he dont ask to solve the problems just reply to the user.",
            expected_output="The solution of the mathematical problems.",
            agent=self.Math_problem_solver_agent,
        )

        self.Mathematical_crew = Crew(
            agents=[self.Math_problem_solver_agent],
            tasks=[self.Math_problem_solving_task],
            verbose=True,
            # memory=True
        )


crew = Mathematical_Crew()

def kickoff():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]: 
            break
        print(crew.Mathematical_crew.kickoff({"user_input":user_input}))

