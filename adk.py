import os
from google import genai
from google.genai import types
from typing import AsyncGenerator, Dict, Any
from input_model import AgentInput

class GoogleADKAgent:
    def __init__(self, api_key=None):
        """Initialize Google ADK client"""
        self.client = genai.Client(
            api_key=api_key or os.getenv('GOOGLE_API_KEY')
        )
        self.model = "gemini-2.0-flash-exp"
    
    async def run_async(self, input_data: AgentInput) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Run agent asynchronously to match your existing agent interface
        """
        # Build prompt based on input
        prompt = self._build_prompt(input_data)
        
        try:
            # Use streaming for real-time responses
            response = self.client.models.generate_content_stream(
                model=self.model,
                contents=prompt
            )
            
            full_response = ""
            async for chunk in response:
                if chunk.text:
                    full_response += chunk.text
            
            yield {
                "formatted_message": full_response,
                "message": full_response
            }
            
        except Exception as e:
            yield {
                "formatted_message": f"Error: {str(e)}",
                "message": f"Error: {str(e)}"
            }
    
    def _build_prompt(self, input_data: AgentInput) -> str:
        """Build prompt from input data"""
        prompt_parts = []
        
        if input_data.subject:
            prompt_parts.append(f"Subject: {input_data.subject}")
        if input_data.topic:
            prompt_parts.append(f"Topic: {input_data.topic}")
        if input_data.doubt:
            prompt_parts.append(f"Question: {input_data.doubt}")
        
        return "\n".join(prompt_parts)