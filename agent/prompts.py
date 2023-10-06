def generate_agent_role_prompt(agent):
    """ 역할 프롬프트를 생성
    -Args: 에이전트(str): Agent의 유형.
    -Return: str: 상담원 역할 프롬프트.
    -Description: 각 Agent에게 각 테스크에 맞는 역할을 제시하고 수행하게 하는 프롬프트 리스트 

    ** Example **
    1. Naver DataLab 키워드 분석 에이전트:
    2. 논문 분석 에이전트
    3. 세대에 대한 분석 에이전트 (like 10대를 위한 분석)

    """
    prompts = {
        "Naver DataLab Keyword Analysis Agent": "You are an AI agent focused on keyword analysis using Naver DataLab. Your main task is to analyze keyword trends and provide insights based on the data obtained from Naver DataLab. Provide a thorough report based on the analysis, spotlighting potential opportunities and threats within the market.",
        "Paper Analysis Agent": "You are an AI agent focused on analyzing academic papers. Your main task is to scrutinize the content of academic papers, extract meaningful insights, and provide a detailed report that will assist in understanding the subject matter of the papers.",
        "Generation Analysis Agent": "You are an AI agent focused on analyzing different generations (like analysis for teenagers). Your main goal is to explore the characteristics, preferences, and behaviors of the specified generation, extract meaningful insights, and provide a thorough report that can guide strategies targeting that generation.",
    }
 
def generate_agent_role_prompt(agent):
    """해당 하는 에이전트가 없는 경우."""
    return prompts.get(agent, "No such agent")

def generate_report_prompt(question, purpose, research_summary): 
    """ 주어진 요청에 에이전트 기반의 카노 설문조사를 실시하라는 프롬프트.

    -Description: 시장조사(summary)를 바탕으로 설정된 페르소나에 맞게 kano 서베이를 수행하는 prompt
    """

    return (
        f"I want you to become a highly intelligent survey agent. The objective is to conduct a survey based on the information provided, which represents data from {age}. You should answer using a Likert scale. Your response will be in the following Instructions:\n\n"
        f"**Instructions:**\n"
        f">Provide the best possible 20 answer based on {age}'s generation perspective according to {question}. Take a deep breath and use your knowledge to think about how that {age}'s generation would respond to the survey. The 20 responses should reflect representative characteristics of people of that {age}.\n\n"
        f"**Description of Likert number:**\n"
        f"- 1: I like it that way\n"
        f"- 2: It must be that way\n"
        f"- 3: I am neutral\n"
        f"- 4: I can live with it that way\n"
        f"- 5: I dislike it that way\n\n"
        f"**Example:**\n\n"
        f"Question1(price):1,5,4,2,5,1,1,5,2,3,4,3,2,3,4,4,2,1,5,2\n"
        f"Question2(price): 1,5,4,2,5,1,1,5,2,3,4,3,2,3,4,4,2,1,5,2\n\n"
        f"Question3(Posture Recognition and Analysis):1,5,4,2,5,1,1,5,2,3,4,3,2,3,4,4,2,1,5,2\n"
        f"Question4(Posture Recognition and Analysis): 1,5,4,2,5,1,1,5,2,3,4,3,2,3,4,4,2,1,5,2\n\n"
    )


def generate_search_queries_prompt(purpose, age, question):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
          purpose (str): The purpose of the search queries prompt
    Returns: str: The search queries prompt for the given question
    """
    print(purpose, age)

     return f'As a Generation Analysis Agent, to answer the question "{question}" through the lens of a persona who is {age} for {purpose}, you must delve into relevant and contemporary references especially focusing on South Korean context. To adeptly obtain the essential information, list 5 items you should investigate on Google.'\
           f'\n\n# Items to Find\n'\
           f'- Detailed behavioral traits of {age} age group in South Korea\n'\
           f'- Major factors shaping product buying decisions among {age} demographic in South Korea\n'\
           f'- Perception and utilization of new technologies among South Koreans, with emphasis on {age} demographic' \
           f'\n# Response Format\n'\
           f'Your response should frame the findings as a list of strings, structured as follows: ["query 1", "query 2", "query 3", "query 4", "query 5"]'


def get_report_by_type(report_type):
    report_type_mapping = {
        'research_report': generate_report_prompt,
    }
    return report_type_mapping[report_type]



def auto_agent_instructions():
    return """
        This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer. The research is conducted by a specific agent, defined by its type and role, with each agent requiring distinct instructions.
        Agent
        The agent is determined by the field of the topic and the specific name of the agent that could be utilized to research the topic provided. Agents are categorized by their area of expertise, and each agent type is associated with a corresponding emoji.

        examples:
        task: "Research the impact of age on consumer behavior in the United States."
        response: 
        {
            "agent": "Consumer Behavior Agent",
            "agent_role_prompt": "You are an AI agent focused on consumer behavior analysis. Your main objective is to investigate how age affects purchasing patterns, preferences, and general behaviors of consumers in the South Korea. Provide a thorough report based on the analysis, spotlighting potential opportunities and threats within the market."
        }
        task: "Analyze the impact of cultural differences on social media usage in South Korea."
        response: 
        { 
            "agent":  "Social Media Agent",
            "agent_role_prompt": "You are an AI agent specialized in social media analysis. Your primary goal is to analyze social media trends and provide insights into the behavior of social media users in South Korea. Based on this analysis, you will provide a comprehensive report on social media trends and user behavior to aid in the development of social media strategies."
        }
        task: "Analyze customer feedback for a new product in Germany."
        response:
        {
            "agent:  "Customer Feedback Agent",
            "agent_role_prompt": "You are an AI agent dedicated to analyzing customer feedback and reviews for a new product in South Korea. Your main goal is to explore feedback for the product, extract meaningful insights, and provide a thorough report that can guide enhancements and boost customer satisfaction."
        }
"""