Multi-Agent Sports Intelligence Framework
(e.g., "Summarize the 2022 World Cup Final") ↓ [Root Agent] SportsFinder (gemini-2.5-flash) Role: Orchestrator & Final Expert Response
 ↓ ├─→ [Sub-Agent] ScoreReporter (gemini-2.5-flash) │   Role: Extraction of raw match data.
 │   Data Found: Argentina 3–3 France (4–2 penalties).
 │   Data Found: 88,966 spectators at Lusail Stadium.
 │   ← (Returns structured scores to Root) │ └─→ [Sub-Agent] SportsAnalyst (gemini-2.5-flash) Role: Qualitative and historical analysis.
 Context: One of the greatest football matches in history.
 Context: Messi's second Golden Ball.
 ← (Returns analytical context to Root) ↓ Final Response to User SportsFinder synthesizes data into a concise expert response (<20 words)
This repository implements a hierarchical multi-agent system designed for the Intelligence Bureau track, specifically focused on converting unstructured sporting narratives into structured intelligence. The system utilizes the Google ADK to analyze complex events, such as the 2022 FIFA World Cup Final.
System Architecture: Agent Orchestration
The core of the system is a hierarchical orchestration model where a primary "Root Agent" manages specialized sub-agents to process data efficiently
.
SportsFinder (Root Agent): Acts as the primary interface. It is configured with an instruction to behave as a sports expert and provide direct, concise responses (under 20 words)
.
ScoreReporter (Sub-Agent): A specialized agent dedicated to finding and extracting specific match scores and statistical outcomes
.
SportsAnalyst (Sub-Agent): A specialized agent focused on qualitative analysis and contextual evaluation
.
In this orchestration, SportsFinder delegates tasks to its sub-agents based on the user's query. For example, if asked about the 2022 Final, it leverages ScoreReporter to identify the 3–3 draw and subsequent 4–2 penalty shoot-out victory for Argentina, while utilizing SportsAnalyst to note that the match is widely considered one of the greatest football matches in history
.
Handling Unstructured Data for Intelligence Bureau
A primary objective of this framework is the transformation of unstructured data—such as journalistic reports and historical summaries—into actionable intelligence.
The match report of the 2022 FIFA World Cup Final serves as the primary unstructured source. The system handles this data through:
Fact Extraction from Narrative: The agents parse dense text to extract specific details like the 88,966 spectators at Lusail Stadium or the record 1.5 billion television viewers
.
Temporal and Event Mapping: The system identifies rapid event sequences within the prose, such as Kylian Mbappé’s 97-second brace in the 81st minute
.
Historical Contextualization: The agents process narrative history to identify rare feats, such as Argentina becoming only the second team in history to win the World Cup after losing their opening match (a 2–1 loss to Saudi Arabia)
.
Entity Recognition and Achievement Tracking: The system captures individual accolades mentioned in the text, such as Lionel Messi winning the Golden Ball and becoming the first player to win the award twice
