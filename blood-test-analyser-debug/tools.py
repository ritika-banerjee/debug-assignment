## Importing libraries and files
import os
from dotenv import load_dotenv
from crewai.tools import tool, BaseTool
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from crewai_tools import SerperDevTool

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class BloodTestReportTool(BaseTool):
    name: str = "BloodTestReportTool"
    description: str = "Tool to read PDF blood test reports. Use without parameters to read default file."
    
    def _run(self, **kwargs):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Blood Test report file
        """
        path = kwargs.get('path', None)
        if path is None:
            path = os.path.join("data", "sample.pdf")
        
        if not os.path.exists(path):
            return f"File not found at path: {path}. Please check if the file exists."
        
        docs = PyPDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content

            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report

## Creating Nutrition Analysis Tool
class NutritionTool(BaseTool):
    name: str = "NutritionTool"
    description: str = "NutritionTool"
    
    def _run(self, blood_report_data):
        # Process and analyze the blood report data
        processed_data = blood_report_data

        # Clean up the data format
        processed_data = ' '.join(processed_data.split())

        # TODO: Implement nutrition analysis logic here
        return "Nutrition analysis functionality to be implemented"

## Creating Exercise Planning Tool
class ExerciseTool(BaseTool):
    name: str = "ExerciseTool"
    description: str = "ExerciseTool"
    
    def _run(self, blood_report_data):        
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"