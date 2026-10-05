from typing import Annotated,TypedDict,List
import operator

class AgentState(TypedDict):
    messages: Annotated[List[str], operator.add]
    current_query:str
    plan: List[str]
    status: str
    final_answer: str
    documents: List[str]

    

