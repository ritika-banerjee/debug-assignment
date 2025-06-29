## Importing libraries and files
from crewai import Task

from agents import doctor, verifier
from tools import search_tool, BloodTestReportTool

## Creating a task to help solve user's query
help_patients = Task(
    description="Analyze the user's query: {query} and provide helpful medical guidance.\n\
Use the blood test report tool to read and analyze any provided blood test reports.\n\
Search the internet for current medical information when needed.\n\
Provide accurate, evidence-based health recommendations.\n\
Focus on identifying any abnormalities in the blood work and explain their significance.",

    expected_output="""Provide a comprehensive medical analysis including:
- Summary of key findings from the blood test report
- Identification of any values outside normal ranges
- Clinical significance of abnormal results
- Evidence-based recommendations for follow-up care
- Relevant and accurate medical information with proper sourcing""",

    agent=doctor,
    tools=[BloodTestReportTool(), search_tool],
    async_execution=False,
)

## Creating a nutrition analysis task
nutrition_analysis = Task(
    description="Analyze blood test results to provide personalized nutrition recommendations.\n\
Review blood markers related to nutrition (glucose, lipids, vitamins, minerals).\n\
Based on user query: {query} and blood test findings, recommend appropriate dietary changes.\n\
Focus on evidence-based nutritional interventions for any identified deficiencies or imbalances.",

    expected_output="""Provide detailed nutrition guidance including:
- Analysis of nutrition-related blood markers
- Specific dietary recommendations based on blood results  
- Foods to include or limit based on findings
- Evidence-based supplement recommendations if indicated
- Meal planning suggestions tailored to blood test results""",

    agent=doctor,
    tools=[BloodTestReportTool(), search_tool],
    async_execution=False,
)

## Creating an exercise planning task
exercise_planning = Task(
    description="Create a safe, personalized exercise plan based on blood test results and health status.\n\
Consider cardiovascular markers, metabolic indicators, and any health conditions.\n\
Address user query: {query} while ensuring exercise recommendations are appropriate for the individual.\n\
Focus on evidence-based exercise prescriptions that support health improvement.",

    expected_output="""Develop a comprehensive exercise plan including:
- Exercise recommendations based on blood test indicators
- Appropriate intensity levels for the individual's health status
- Specific activities targeting identified health concerns
- Safety considerations and contraindications
- Progressive plan with realistic, achievable goals""",

    agent=doctor,
    tools=[BloodTestReportTool(), search_tool],
    async_execution=False,
)

    
verification = Task(
    description="Verify that the provided document is a legitimate blood test report.\n\
Carefully analyze the document structure, medical terminology, and format.\n\
Confirm the presence of standard blood test parameters and laboratory information.",

    expected_output="""Provide verification results including:
- Confirmation of document type (blood test report or other)
- Analysis of document authenticity and completeness
- Summary of key blood parameters present in the report
- Assessment of report quality and readability for analysis""",

    agent=verifier,
    tools=[BloodTestReportTool()],
    async_execution=False
)