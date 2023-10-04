def generate_agent_role_prompt(agent):
    """ Generates the agent role prompt.
    Args: agent (str): The type of the agent.
    Returns: str: The agent role prompt.
    
    ** 에이전트를 전반적으로 수정하였음 **

    목적: 신제품 안마의자를 기획하는 상황에서 소비자들의 반응이나 특성을 기반으로 설문을 진행할 예정. 이를 위한 UXResearch.
    
    """
    prompts = {
        "Consumer Behavior Agent": "You are an AI agent focused on consumer behavior analysis. Your main objective is to investigate purchasing patterns, preferences, and general behaviors of consumers in relation to specific products or market categories. Provide a thorough report based on the analysis, spotlighting potential opportunities and threats within the market.",
        "Competitor Analysis Agent": "You are an AI agent focused on competitor analysis. Your main task is to scrutinize competitor products, pricing, and marketing strategies, and provide a detailed report that will assist in positioning our product effectively within the market, identifying potential advantages and areas for improvement.",
        "Customer Feedback Agent": "You are an AI agent dedicated to analyzing customer feedback and reviews. Your main goal is to explore feedback for existing products or services, extract meaningful insights, and provide a thorough report that can guide enhancements and boost customer satisfaction.",
        "New Product Development Agent": "You are an AI agent specialized in market analysis for new product development. Your primary goal is to analyze the characteristics of current consumers, their preferences, and the features they prefer in products. For example, you may analyze whether they prefer voice recognition features. Based on this analysis, you will provide a comprehensive report on the market trends and consumer preferences to aid in the development of new products.",
        "Social Media Agent": "You are an AI agent specialized in social media analysis. Your primary goal is to analyze social media trends and provide insights into the behavior of social media users. Based on this analysis, you will provide a comprehensive report on social media trends and user behavior to aid in the development of social media strategies.",
        "Marketing Agent": "You are an AI agent specialized in marketing analysis. Your primary goal is to analyze marketing trends and provide insights into the behavior of consumers. Based on this analysis, you will provide a comprehensive report on marketing trends and consumer behavior to aid in the development of marketing strategies.",
        "Market Research Agent": "You are an AI agent specialized in market research. Your primary goal is to analyze market trends and provide insights into consumer behavior. Based on this analysis, you will provide a comprehensive report on market trends and consumer behavior to aid in the development of market strategies.",
    }

def generate_agent_role_prompt(agent):
    """ Generates the agent role prompt.
    Args: agent (str): The type of the agent.
    Returns: str: The agent role prompt.
    """
    return prompts.get(agent, "No such agent")

def generate_report_prompt(question, purpose, research_summary): 
    """ Generates the report prompt for the given question and research summary.
    Args: question (str): The question to generate the report prompt for
            research_summary (str): The research summary to generate the report prompt for
            purpose (str): The purpose of the research summary
    Returns: str: The report prompt for the given question and research summary
   
    """

    return (
        f"As a person in their {age}s residing in Korea, you have a deep understanding of the characteristics " 
        f"and nuances of your age group. Your specialization is in conducting Kano surveys. "
        f"Your task is to address the following question: '{question}'. Please refer to the "
        f"meanings of the Likert scale numbers provided below before responding. Ensure the "
        f"accuracy of the persona and respond to the survey accordingly.\n\n"
        F"product: Massage chair"
        f"Context: {research_summary}\n\n"
        f"Meaning of Likert Scale:\n"
        f"- 1: Strongly Agree\n"
        f"- 2: Agree\n"
        f"- 3: Neutral\n"
        f"- 4: Disagree\n"
        f"- 5: Strongly Disagree\n\n"
        f"Your response should be 20 response on each question based on a persona who is {age}. Please answer in the form of Likert numbers and follow the format below:\n"
        f"Question: 2,4,1,5,3,3,2,4,4,2,1,5,5,1,5,1,2,4,4,2\n"
        f"Question: 2,4,1,5,3,3,2,4,4,2,1,5,5,1,5,1,2,4,4,2\n\n"
    )


def generate_search_queries_prompt(purpose, age):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
          purpose (str): The purpose of the search queries prompt
    Returns: str: The search queries prompt for the given question
    
    """
    print(purpose, age)

    return f'To accomplish {purpose} for {age}, you need to gather references from 2022 ~ 2023 to know about {age} well. To efficiently obtain the required information, list 5 items you should search for on Google.'\
           f'\n\n# Items to Find\n'\
           f'- Characteristics related to {age} in South Korea\n'\
           f'- Factors influencing product purchasing decisions in South Korea for {age} demographic\n'\
           f'- What Koreans think about new technologies' \
           f'\n# Response Format\n'\
           f'Your response should be a list of strings in the following format: ["query 1", "query 2", "query 3", "query 4", "query 5"]'


# def generate_report_prompt(question, purpose, research_summary): 
#     """ Generates the report prompt for the given question and research summary.
#     Args: question (str): The question to generate the report prompt for
#             research_summary (str): The research summary to generate the report prompt for
#     Returns: str: The report prompt for the given question and research summary
   
#    **추가된 부분 
#    -{purpose}내용을 추가.
#    Purpose(목적의 예시: 신제품을 소비하는 10대의 특성을 파악하여 신제품에 대한 PMF를 파악하기 위해)에 기반한 Research summary를 활용하여
#    {question}을 수행해줘.
   
   
#     """

#     return f'"""{research_summary}""" Using the above information for {purpose}, answer the following'\
#            f' question or topic: "{question}" in Likert 1-5 response. you should answer one answer of each question. --'\
#            f' Your response should be based on the persona that the user requires.' \
#            f' Meaning of the Likert numbers:'\
#            f' - 1: Strongly agree'\
#            f' - 2: Agree'\
#            f' - 3: Neutral'\
#            f' - 4: Disagree'\
#            f' - 5: Strongly disagree.'\
#            f' Write all used source URLs at the end of the report in APA format.'

# def generate_search_queries_prompt(question):
#     """ Generates the search queries prompt for the given question.
#     Args: question (str): The question to generate the search queries prompt for
#     Returns: str: The search queries prompt for the given question
    
#       **추가된 부분 
#    - 여기에서 검색이 {question:설문조사}가 아니라 {purpose}가 들어가야함. 그로 인해 구글 검색이 목적에 맞게 최적의 구글 쿼리를 4가지를 뽑게 됨.
#    **Take a deep breath prompt 추가하여 검색의 결과를 더 잘 도출하게 Prompt 작성. **
    
#     """

#     return f'Take a deep breath and work on this problem step-by-step.'\
#            f'Write 4 google search queries to search online that form an objective opinion from the following: "{question}"'\
#            f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3", "query 4"]'


# def generate_resource_report_prompt(question, research_summary):
#     """Generates the resource report prompt for the given question and research summary.

#     Args:
#         question (str): The question to generate the resource report prompt for.
#         research_summary (str): The research summary to generate the resource report prompt for.

#     Returns:
#         str: The resource report prompt for the given question and research summary.
    
#     """
#     return f'"""{research_summary}""" Based on the above information, generate a bibliography recommendation report for the following' \
#            f' question or topic: "{question}". The report should provide a detailed analysis of each recommended resource,' \
#            ' explaining how each source can contribute to finding answers to the research question.' \
#            ' Focus on the relevance, reliability, and significance of each source.' \
#            ' Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax.' \
#            ' Include relevant facts, figures, and numbers whenever available.' \
#            ' The report should have a minimum length of 1,200 words.'


# def generate_outline_report_prompt(question, research_summary):
#     """ Generates the outline report prompt for the given question and research summary.##설문조사를 수행해줘
#     Args: question (str): The question to generate the outline report prompt for
#             research_summary (str): The research summary to generate the outline report prompt for
#     Returns: str: The outline report prompt for the given question and research summary ## 설문조사 수행한 결과를 result로 제공해줘.
#     """

#     return f'"""{research_summary}""" Using the above information, generate an outline for a research report in Markdown syntax'\
#            f' for the following question or topic: "{question}". The outline should provide a well-structured framework'\
#            ' for the research report, including the main sections, subsections, and key points to be covered.' \
#            ' The research report should be detailed, informative, in-depth, and a minimum of 1,200 words.' \
#            ' Use appropriate Markdown syntax to format the outline and ensure readability.'

# def generate_concepts_prompt(purpose, research_summary):
#     """ Generates the concepts prompt for the given purpose.
#     Args: purpose (str): The purpose to generate the concepts prompt for
#             research_summary (str): The research summary to generate the concepts prompt for
#     Returns: str: The concepts prompt for the given purpose

#     Generate 5 types of highly intelligent expert opinions from Product Managers. 
#     Format: 
#     ex) 
#     Expert 1: 
#     Expert 2:
#     """

#     return f'"""{research_summary}""" Using the above information, generate a list of 5 highly intelligent expert opinions from Product Managers'\
#            f' on the following purpose: "{purpose}". The list should provide a well-structured framework.'\
#            ' You must respond with a list of strings in the following format: ["Expert 1: ", "Expert 2: ", "Expert 3: ", "Expert 4: ", "Expert 5: "]'




def generate_lesson_prompt(concept):
    """
    Generates the lesson prompt for the given question.
    Args:
        concept (str): The concept to generate the lesson prompt for.
    Returns:
        str: The lesson prompt for the given concept.


    ** 수정요청:
    수정되어야할 함수 안의 프롬프트: 5가지의 concept을 바탕으로 해당 함수를 설문조사를 시행한 페르소나에 대한 설명을 적어줬으면 좋겠어. 해당 페르소나가 어떠한 특성을 가지고 있는지 신제품에 대해서 어떻게 느끼는지 등,
    """

    prompt = f'Using the 5 concepts you generated, generate a comprehensive lesson for persona about a new product related to {concept}. '\
             'The survey should include questions about the persona\' characteristics and how they feel about the product. '\
             'The survey should be well-structured, informative, and in-depth, with a minimum of 1,200 words. '\
             'Use appropriate Markdown syntax to format the survey and ensure readability.'

    return prompt

### **이 부분은 아마 Research Report만 있으면 될듯? **
def get_report_by_type(report_type):
    report_type_mapping = {
        'research_report': generate_report_prompt,
    }
    return report_type_mapping[report_type]

# def generate_survey_answer_prompt(surveyForm, research_summary):
#     # 설문조사를 답변하는 프롬프트 작성
#     """ Generates the report prompt for the given question and research summary.
#     Args: question (str): The question to generate the report prompt for
#             research_summary (str): The research summary to generate the report prompt for
#     Returns: str: The report prompt for the given question and research summary
#     """

#     # 해당 prompt를 수정해야함
#     # return f'"""{research_summary}""" Using the above information, answer the following'\
#     #        f' question or topic: "{surveyForm}" in a detailed report --'\
#     #        " The report should focus on the answer to the question, should be well structured, informative," \
#     #        " in depth, with facts and numbers if available, a minimum of 1,200 words and with markdown syntax and apa format. "\
#     #         "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions." \
#     #        "Write all used source urls at the end of the report in apa format"
#     return f'"""{research_summary}""" Using the above information, answer the following'\
#         f' question or topic: "{surveyForm}" --' \
#                   """.The survey will utilize a 5-point Likert scale for responses.
#        Meaning of the Likert numbers:
#        - 1: Strongly agree
#        - 2: Agree
#        - 3: Neutral
#        - 4: Disagree
#        - 5: Strongly disagree"""

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