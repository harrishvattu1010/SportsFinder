from google.adk.agents import LlmAgent

score_reporter = LlmAgent(name="ScoreReporter", model="gemini-2.5-flash", instruction="Find scores.")
sports_analyst = LlmAgent(name="SportsAnalyst", model="gemini-2.5-flash", instruction="Analyze.")

root_agent = LlmAgent(
    name="SportsFinder",
    model="gemini-2.5-flash", 
    instruction="You are a sports expert. Answer the user directly in under 20 words.",
    sub_agents=[score_reporter, sports_analyst]
)
