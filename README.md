<h1>AI Enabled Research Assistant</h1>

Before starting any research project, conducting a literature survey is the most strenuous part. Having to scour IEEE or any publication repository is time-consuming. Hence this application will streamline the process by displaying all the related papers in one go. The application has a memory layer associated with the user id and uses GPT-4o-mini and a vector database to search for relevant research papers based on your query. 

### Technologies Used
- [Multion](https://www.multion.ai/): 
  To embed AI agents.
- [mem0](https://github.com/mem0ai/mem0): 
  For adding the memory layer which saves the user's previous searches.
- [streamlit](https://streamlit.io/):
  For the user interface
- [OpenAI](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/):
  To create chats using GPT-4o-mini

### Usage
Enter your OpenAI and MultiOn API keys in the text inputs.
<img width="914" alt="Screenshot 2024-07-27 at 10 51 50 PM" src="https://github.com/user-attachments/assets/cbcf5eab-fa8f-4802-ac9f-55b59bc99118">

Once your API key is verified, enter your search query. You will thus be able to see the research papers in the given format, streamlining literature survey. 
<img width="887" alt="Screenshot 2024-07-27 at 10 51 45 PM" src="https://github.com/user-attachments/assets/7c2ce899-8bfb-4d9e-8cc0-16dcf9820797">

### Installation

1. Git clone the repository on your device
   ```
   git clone https://github.com/mansidhamne/AI_Research_Agent.git
   ```
3. Set up a virtual environment
   ```
   python -m venv venv
   ```
4. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the following command on your terminal (Ensure Docker Desktop is running)
   ```
   docker run -p 6333:6333 -d qdrant/qdrant
   ```
6. Run the streamlit application
   ```
   streamlit run app.py
   ```
