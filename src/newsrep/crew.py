from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from openai import OpenAI

# ==========================
# NewsRep Crew Class
# ==========================

@CrewBase
class Newsrep():
    """Newsrep Crew: Gathers, Optimizes, and Writes News"""

    # Load configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ==========================
    # Agents Setup
    # ==========================

    @agent
    def web_searcher(self) -> Agent:
        """Creates the Web Searcher agent with an internet search tool"""
        return Agent(
            config=self.agents_config['web_searcher'],
            tools=[SerperDevTool(n_results=5)],  # Integrate SerperDevTool
            verbose=True
        )

    @agent
    def news_optimizer(self) -> Agent:
        """Creates the News Optimizer agent using Gemini Flash 1.5"""
        return Agent(
            config=self.agents_config['news_optimizer'],
            # llm="gemini-flash-1.5",  # Use Google Gemini AI for optimization
            verbose=True
        )

    @agent
    def news_writer(self) -> Agent:
        """Creates the News Writer agent"""
        return Agent(
            config=self.agents_config['news_writer'],
            verbose=True
        )

    # ==========================
    # Tasks Setup
    # ==========================

    @task
    def web_research_task(self) -> Task:
        """Task for gathering the latest news from the web"""
        return Task(
            config=self.tasks_config['web_research_task'],
        )

    @task
    def news_optimization_task(self) -> Task:
        """Task for optimizing raw news data"""
        return Task(
            config=self.tasks_config['news_optimization_task'],
        )

    @task
    def news_writing_task(self) -> Task:
        """Task for generating a structured news article"""
        return Task(
            config=self.tasks_config['news_writing_task'],
            # output_file='final_news.md'
        )

    # ==========================
    # Crew Setup
    # ==========================

    @crew
    def crew(self) -> Crew:
        """Creates the Newsrep Crew with agents and tasks"""
        return Crew(
            agents=self.agents,  # Auto-created by @agent decorators
            tasks=self.tasks,  # Auto-created by @task decorators
            process=Process.sequential,  # Run tasks in order
            verbose=True
        )
